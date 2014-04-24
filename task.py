import datetime
import subprocess

class Task(object):
    id = None
    date = None
    command = None
    priority = None
    executed = None
    correct = None
    def __init__(self, command, priority=None):
        
        if not priority:
            priority = 1

        self.date = datetime.datetime.now()
        self.command = command
        self.priority = priority
        self.executed = False
        self.correct = False

    def execute(self):
        output = subprocess.Popen(['nslookup', self.dominio], 
                stdout = subprocess.PIPE).communicate()[0]