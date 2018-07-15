from pm.postmaster import PostMaster
from utils.myconfigparser import MyConfigParser
import psutil
import time
import re


class ProcMonitor:
    pattern = ''
    ps_lst = []
    post_master = None
    config = None

    def __init__(self, pattern):
        self.pattern = pattern

        # Obtain information from the configuration file
        self.parser = MyConfigParser()
        self.parser.read("setup.cfg")
        from_email = self.parser.get_from_email()
        password = self.parser.get_password()
        to_email = self.parser.get_to_email()

        self.post_master = PostMaster("Hello", "Hello world!", from_email, password, to_email)

    class MyProcess:
        _name = ""
        _pid = -1

        def __init__(self, name, pid):
            self._name = name
            self._pid = pid

        def pid(self):
            return self._pid

        def name(self):
            return self._name

    def run(self):
        if self.pattern == '':
            return

        while True:
            time.sleep(5)
            # Check that the processes recorded in the list are still available in the system
            pids = psutil.pids()

            new_list = []
            new_pid_list = []
            for ps in self.ps_lst:
                if ps.pid() not in pids:
                    self.post_master.send()
                    print(ps.name() + "has just stopped!")
                else:
                    new_list.append(ps)
                    new_pid_list.append(ps.pid())
            # replace the old list
            self.ps_lst = new_list
            pid_list = new_pid_list

            for proc in psutil.process_iter():
                rtn_obj = re.match(self.pattern, proc.name())

                if rtn_obj:
                    if proc.pid not in pid_list:
                        self.ps_lst.append(self.MyProcess(proc.name(), proc.pid))
                        pid_list.append(proc.pid)
                        print(proc.name() + "has been added to the monitor list")





