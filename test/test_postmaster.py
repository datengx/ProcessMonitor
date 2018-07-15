import unittest
from pm.postmaster import PostMaster
from utils.myconfigparser import MyConfigParser


class TestPostMaster(unittest.TestCase):

    def test_send(self):
        config = MyConfigParser()
        config.read("../setup.cfg")

        subject = "Greetings!"
        text = "Hello World!"
        from_address = config.get_from_email()
        password = config.get_password()
        to_address = config.get_to_email()

        pm = PostMaster(text, subject, from_address, password, to_address)
        pm.send()
        self.assertRaises(Exception)
