import unittest
from pm.postmaster import PostMaster


class TestPostMaster(unittest.TestCase):

    def test_send(self):
        text = "Hello World!"
        fromaddr = "sammy556631@hotmail.com"
        toaddr = "da_teng0702@hotmail.com"

        pm = PostMaster(text, fromaddr, toaddr)
        pm.send()
        self.assertRaises(Exception)
