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
    template = "{ps_name} has just stopped running.\n" \
               "\n" \
               "ps name: {ps_name}\n" \
               "pid: {pid}\n"

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
        _create_time = -1.0

        def __init__(self, name, pid, create_time):
            self._name = name
            self._pid = pid
            self._create_time = create_time

        def pid(self):
            return self._pid

        def name(self):
            return self._name

        def create_time(self):
            return self._create_time

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
                    subject = "{ps_name} just finished!".format(ps_name=ps.name())
                    text = self.template.format(ps_name=ps.name(), pid=ps.pid())

                    self.post_master.set_subject(subject)
                    self.post_master.set_text(text)

                    self.post_master.send()
                    print(ps.name() + " has just stopped!")
                else:
                    new_list.append(ps)
                    new_pid_list.append(ps.pid())
            # replace the old list
            self.ps_lst = new_list
            pid_list = new_pid_list

            for proc in psutil.process_iter():
                rtn_obj = re.match(self.pattern, proc.name())

                if rtn_obj:
                    if not self.monitored(proc, pid_list, self.ps_lst):
                        self.ps_lst.append(self.MyProcess(proc.name(), proc.pid, proc.create_time()))
                        pid_list.append(proc.pid)
                        print(proc.name() + " has been added to the monitor list")

    def monitored(self, ps, pid_lst, ps_lst):

        if ps.pid in pid_lst:
            # The process with the same PID must be the same
            return True
        else:
            for pp in ps_lst:
                d = ps.create_time() - pp.create_time()
                if d < 50 and d > -50 and ps.name() == pp.name():
                    return True
            return False
