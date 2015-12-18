import os
from gpgkey import GPGkey

class PyPass:

    #Creates a PyPass object
    def __init__(self, config):
        self.gpass_config = config
        self.gpg = GPGkey(self.gpass_config.gpgbinary, self.gpass_config.gpghome, self.gpass_config.gpgkey)

    #Returns an unecrypted string of the selected file
    def account(self, account):
        out = self.gpg.decrypt_from_file(self.build_path(account))
        return str(out)

    #Inserts a GPG encrypted file into the password store
    def insert(self, account, message):
        if not str1.endswith('\n'):
            message += '\n'
        print "Entering Insert"
        out = self.gpg.encrypt_to_file(message, self.build_path(account))

    #Deletes the selected account
    def delete(self, account):
        os.remove(self.build_path(account))
        print "pass delete ", self.build_path(account)

    #Displays the folders and accounts in the selected folder
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

    #Returns an array of the items in the directory location
    def pass_array(self, child_path = ""):
        dir_items = self.build_dir(self.build_path(child_path))
        return dir_items

    #Concatinates the root password store path with the child path
    def build_path(self, child_path):
        return self.gpass_config.password_store + '/' + child_path
    
