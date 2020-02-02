from hello_world.formater import plain_text_upper_case
from hello_world.formater import plain_text_lower_case
from hello_world.formater import plain_text
from hello_world.formater import format_to_json
from hello_world.formater import format_to_xml
import unittest


class TestFormater(unittest.TestCase):
    def test_plain_text(self):
        r = plain_text("msg", "imie")
        self.assertEquals("imie msg", r)

    def test_plain_lowercase(self):
        r = plain_text_lower_case("WWIMIE", "EEEMSG")
        name = r.split(" ")[0]
        msg = r.split(" ")[1]
        self.assertTrue(name.islower())
        self.assertTrue(msg.islower())

    def test_plain_uppercase(self):
        r = plain_text_upper_case("WWIMIE", "EEEMSG")
        name = r.split(" ")[0]
        msg = r.split(" ")[1]
        self.assertTrue(name.isupper())
        self.assertTrue(msg.isupper())

    def test_json(self):
        r = format_to_json("msg", "imie")
        self.assertEquals('{"imie": "imie", "msg": "msg"}', r)

    def test_xml(self):
        r = format_to_xml("msg", "imie")
        self.assertEquals('<?xml version="1.0" encoding="UTF-8" ?>'
                          '<greetings><msg>msg</msg><name>imie</name>'
                          '</greetings>', r)
