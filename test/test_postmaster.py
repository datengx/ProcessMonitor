import unittest
from pm.postmaster import PostMaster


class TestPostMaster(unittest.TestCase):

    def test_send(self):
        subject = "Greetings!"
        text = "Hello World!"
        from_address = "sammy556631@hotmail.com"
        to_address = "da_teng0702@hotmail.com"

        pm = PostMaster(text, subject, from_address, to_address)
        pm.send()
        self.assertRaises(Exception)
