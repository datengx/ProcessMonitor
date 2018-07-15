from utils.myconfigparser import MyConfigParser
import unittest


class TestParser(unittest.TestCase):

    def test_init_parser(self):
        parser = MyConfigParser()
        self.assertRaises(Exception)

    def test_read_file(self):
        parser = MyConfigParser()
        parser.read('../setup.cfg')
        self.assertRaises(Exception)

    def test_print(self):
        parser = MyConfigParser()
        parser.read('../setup.cfg')
        print(parser.get_name())
        print(parser.get_from_email())
        print(parser.get_to_email())
        print(parser.get_phone_number())
        print(parser.get_password())
        self.assertRaises(Exception)

