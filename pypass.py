import os
import shlex
from subprocess import Popen, PIPE
from gpgkey import GPGkey

class PyPass:
    #returns an unecrypted string of the selected file
    def account(self, account):
        out = self.gpg.decrypt_from_file(self.location + '/' + account + '.gpg')
        return str(out)

    #TODO: rewrite to use gnupg lib
    def insert(self, account, message):
        out = self.gpg.encrypt_to_file(message, self.location + '/' + account + '.gpg')
        print out
        #return out

    #TODO: rewrite to use gnupg lib
    def generate(self, account):
        print "pass generate ", account

    #TODO: rewrite to use gnupg lib
    def update(self, account, password='', metadata=None):
        print "pass update ", account


    def delete(self, account):
        print "pass delete ", account

    def build_dir(self, path):
        rtn = []
        #pulls the current
        stream = os.listdir(path)
        stream.sort()
        for x in stream:
            #Skip hiden files
            if not x.startswith("."):
                #checks if x is a file
                if not os.path.isdir(path + "/" + x):
                    file_name = x[:-4]
                    rtn.append(file_name)
                else:
                    #print "else -> " + path + "/" + x
                    rtn.append(x + "/")
        rtn.sort()
        return rtn

    def pass_array(self, p = ""):
        path = ""
        if len(p) > 0:
            path = "/"
        path += p
        dirarray = self.build_dir(self.location + path)
        return dirarray

    def __init__(self, gpg_location = "", pass_location = ""):
        self.gpgbinary = '/usr/bin/gpg2'
        self.gpgkey_id = 'cmo.uwp.2010@gmail.com'
        self.gpg_home = os.environ['HOME'] + '/.gnupg'
        self.location = os.environ['HOME'] + '/.password-store'
        if gpg_location != "":
            self.gpg_home = gpg_location
        self.gpg = GPGkey(self.gpgbinary, self.gpg_home, self.gpgkey_id)
        if pass_location != "":
            self.location = pass_location

        #print 'HOME: ' + self.location
