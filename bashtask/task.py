import datetime
import subprocess
import os

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

    def _parse_command(self):
        #TODO
        abierto = False
        cerrado = False
        splitted = self.command.split(' ')
        self.command_splitted = []
        new_part = ''
        for part in splitted:
            if abierto and part.endswith('"'):
                 pass #if part.startswit

    def start(self):
        """
        splitted = self.command.split(' ')
        new_command = list()
        for part in splitted:
            part = part.strip('" ')
            new_command.append(part)
        print new_command

        output = subprocess.Popen(new_command, 
            stdout = subprocess.PIPE).communicate()[0]
        return output
        """
        #output = os.system(self.command)
        output = subprocess.call(self.command, shell=True)
        if output == 0:
            return "All right"
        else:
            return "There is any problem"
        
