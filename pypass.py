import os
import shlex
from subprocess import Popen, PIPE
import gnupg
from gpgkey import GPGkey

class PyPass:
    #TODO: rewrite to use gnupg lib
    def account(self, account):
        cmd = "pass " + account
        #print cmd
        parsed_cmd = shlex.split(cmd)
        proc = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
        out, err = proc.communicate()
        return out

    #TODO: rewrite to use gnupg lib
    def insert(self, account, password):
        cmd = "pass insert -e " + account
        #print cmd
        parsed_cmd = shlex.split([cmd, password, password])
        proc = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
        out, err = proc.communicate()
        return out

    #TODO: rewrite to use gnupg lib
    def generate(self, account):
        print "pass generate ", account

    #TODO: rewrite to use gnupg lib
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

    def __init__(self, gpg_location = "", pass_location = ""):
        gpg_home = os.environ['HOME'] + '/.gnupg'
        self.location = os.environ['HOME'] + '/.password-store'
        if gpg_location != "":
            gpg_home = gpg_location
        self.gpg = GPGkey(gpg_home)
        print public_keys
        if pass_location != "":
            self.location = pass_location

        #print 'HOME: ' + self.location
