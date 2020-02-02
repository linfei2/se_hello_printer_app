.PHONY: test
.DEFAULT_GOAL := test

SERVICE_NAME=hello-world-printer
DOCKER_NAME=$(SERVICE_NAME)
USERNAME=bialekino
TAG=$(USERNAME)/$(DOCKER_NAME):$$(git describe --tags)

tag:
	@echo $(TAG)

deps:
	pip install -r requirements.txt; \
	pip install -r test_requirements.txt

lint:
	flake8 hello_world test

test:
	PYTHONPATH=. py.test  --verbose -s

run:
	python main.py

docker_build:
	docker build -t $(DOCKER_NAME) .

docker_run: docker_build
	docker run \
		--name $(SERVICE_NAME)-dev \
		-p 5000:5000 \
		-d $(DOCKER_NAME)

docker_stop:
	docker stop $(SERVICE_NAME)-dev

docker_push: docker_build
	@docker login --username $(USERNAME) --password $${DOCKER_PASSWORD}; \
	docker tag $(DOCKER_NAME) $(TAG); \
	docker push $(TAG); \
	docker logout