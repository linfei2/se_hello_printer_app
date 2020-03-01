import unittest
import json
from dicttoxml import dicttoxml
from hello_world import app
from hello_world.formater import SUPPORTED


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        ','.join(SUPPORTED) in rv.data

    def test_msg_with_output(self):
        rv = self.app.get('/?output=json')
        output = {
            "imie": "Bartosz",
            "msg": "Hello World!"
        }

        self.assertEquals(json.dumps(output), rv.data)

    def test_msg_with_xml_output(self):
        rv = self.app.get('/?output=xml')
        output = {
            "name": "Bartosz",
            "msg": "Hello World!"
        }

        xml = dicttoxml(output,
                        root=True,
                        custom_root="greetings",
                        cdata=False,
                        attr_type=False)

        self.assertEquals(xml.decode('utf-8'), rv.data)

    def test_msg_with_name_json_output(self):
        rv = self.app.get('/?output=json&name=apolonia')
        output = {
            "imie": "apolonia",
            "msg": "Hello World!"
        }

        self.assertEquals(json.dumps(output), rv.data)
