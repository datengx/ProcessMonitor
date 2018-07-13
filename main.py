from pm.procmonitor import ProcMonitor
from pm.postmaster import PostMaster
from utils.myconfigparser import MyConfigParser


text = "Hello World!"
from_address = "dateng.cognex@gmail.com"
to_address = "da_teng0702@hotmail.com"

pm = PostMaster(text, from_address, to_address)
pm.send()