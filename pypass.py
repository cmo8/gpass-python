import os
import shlex
from subprocess import Popen, PIPE
from gpgkey import GPGkey
class PyPass:

    #returns an unecrypted string of the selected file
    def account(self, account):
        out = self.gpg.decrypt_from_file(self.gpass_config.password_store + '/' + account)
        return str(out)

    #Inserts a GPG encrypted file into the password store
    def insert(self, account, message):
        print "Entering Insert"
        out = self.gpg.encrypt_to_file(message, self.gpass_config.password_store + '/' + account)

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
        dirarray = self.build_dir(self.gpass_config.password_store + path)
        return dirarray

    def __init__(self, config):
        self.gpass_config = config
        self.gpg = GPGkey(self.gpass_config.gpgbinary, self.gpass_config.gpghome, self.gpass_config.gpgkey)
