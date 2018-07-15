from pm.procmonitor import ProcMonitor
from pm.postmaster import PostMaster
from utils.myconfigparser import MyConfigParser
import re
import psutil

# for proc in psutil.process_iter():
#     if re.match("^Subl", proc.name()):
#         print(proc.name())
pm = ProcMonitor("^Sublime")
pm.run()