import os
import shlex
from subprocess import Popen, PIPE
#import gnupg

class PyPass:

    def account(self, account):
        cmd = "pass " + account
        #print cmd
        parsed_cmd = shlex.split(cmd)
        proc = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
        out, err = proc.communicate()
        return out

    def insert(self, account, password):
        cmd = "pass insert -e " + account
        #print cmd
        parsed_cmd = shlex.split([cmd, password])
        proc = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
        out, err = proc.communicate()
        return out

    def generate(self, account):
        print "pass generate ", account

    def update(self, account, password='', metadata=None):
        print "pass update ", account

    def delete(self, account):
        print "pass delete ", account

    def build_dir(self, path):
        rtn = {}
        #pulls the current
        stream = os.listdir(path)
        stream.sort()
        for x in stream:
            if not x.startswith("."):
                if not os.path.isdir(path + "/" + x):
                    index = x[:-4]
                    rtn[index] = path + '/' + x
                else:
                    #print "else -> " + path + "/" + x
                    rtn[x] = self.build_dir(path + "/" + x)
        return rtn

    def pass_array(self, p = ""):
        path = ""
        if len(p) > 0:
            path = "/"
        path += p
        dirarray = self.build_dir(self.location + path)
        return dirarray

    def __init__(self, location=""):
        if location == "":
            self.location = os.environ['HOME'] + '/.password-store'
        else:
            self.location = location
        #print 'HOME: ' + self.location
