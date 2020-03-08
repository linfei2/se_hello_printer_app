# Simple Flask App [![Build Status](https://travis-ci.com/bartoszbialecki/se_hello_printer_app.svg?branch=master)](https://travis-ci.com/bartoszbialecki/se_hello_printer_app) [![Uptime Status](https://app.statuscake.com/button/index.php?Track=mtybpdFKaQ&Days=1&Design=2)](https://www.statuscake.com)

Aplikacja dydaktyczna wyświetlająca imię i wiadomość w różnych formatach dla zajęć
o Continuous Integration, Continuous Delivery i Continuous Deployment.

- Rozpoczynając pracę z projektem (wykorzystując virtualenv). Hermetyczne środowisko dla pojedynczej aplikacji w python-ie:

  ```
  # centos, add to ~/.bashrc
  $ source /usr/bin/virtualenvwrapper.sh

  # ubuntu, add to ~/.bashrc
  $ source /usr/local/bin/virtualenvwrapper.sh

  # tworzymy hermetyczne środowisko dla bibliotek aplikacji:
  $ mkvirtualenv wsb-simple-flask-app
  $ pip install -r requirements.txt
  $ pip install -r test_requirements.txt
  ```

  Sprawdź: [documentację virtualenvwrappera](https://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html)s oraz [biblioteki flask](http://flask.pocoo.org).

- Uruchamianie applikacji:

  ```
  # jako zwykły program
  $ python main.py

  # albo:
  $ PYTHONPATH=. FLASK_APP=hello_world flask run
  ```

- Uruchamianie testów (see: http://doc.pytest.org/en/latest/capture.html):

  ```
  $ PYTHONPATH=. py.test
  $ PYTHONPATH=. py.test  --verbose -s
  ```

- Kontynuując pracę z projektem, aktywowanie hermetycznego środowiska dla aplikacji py:

  ```
  $ source /usr/local/bin/virtualenvwrapper.sh # nie trzeba, jeśli już w .bashrc
  $ workon wsb-simple-flask-app

  ...

  # deaktywacja virtualenv
  $ deactivate
  ```

- Integracja z TravisCI:

  ```
  # stwórz plik .travis.yml i dodaj do niego następujące dane:
  language: python
  python:
  - '2.7'
  ```


# Pomocnicze

## Ubuntu

- Instalacja python virtualenv i virtualenvwrapper:

  ```
  $ sudo pip install virtualenv
  $ sudo pip install virtualenvwrapper
  ```

- Instalacja dockera: [dockerce howto](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

## Centos

- Instalacja python virtualenv i virtualenvwrapper:

  ```
  $ yum install -y python-pip
  $ pip install -U pip
  $ pip install virtualenv
  $ pip install virtualenvwrapper
  ```

- Instalacja docker-a:

  ```
  $ yum remove docker \
        docker-common \
        container-selinux \
        docker-selinux \
        docker-engine

  $ yum install -y yum-utils

  $ yum-config-manager \
      --add-repo \
      https://download.docker.com/linux/centos/docker-ce.repo

  $ yum makecache fast
  $ yum install -y docker-ce
  $ systemctl start docker
  ```

# Materiały

- https://virtualenvwrapper.readthedocs.io/en/latest/
