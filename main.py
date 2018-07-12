from pm.procmonitor import ProcMonitor
from pm.postmaster import PostMaster
from utils.myconfigparser import MyConfigParser


text = "Hello World!"
fromaddr = "dateng.cognex@gmail.com"
toaddr = "da_teng0702@hotmail.com"

pm = PostMaster(text, fromaddr, toaddr)
pm.send()