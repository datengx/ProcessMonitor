from pm.procmonitor import ProcMonitor
from pm.postmaster import PostMaster
from utils.myconfigparser import MyConfigParser
import re
import psutil

# for proc in psutil.process_iter():
#     if re.match("^Code", proc.name()):
#         print(proc.name())
#         print(proc.create_time())
#         print("\n")
pm = ProcMonitor("^Code")
pm.run()