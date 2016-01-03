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
        if not message.endswith('\n'):
            message += '\n'
        print "Entering Insert"
        out = self.gpg.encrypt_to_file(message, self.build_path(account))

    #Deletes the selected account
    def delete(self, account):
        if not os.path.isdir(self.build_path(account)):
            os.remove(self.build_path(account))
            print "Deleted: ", self.build_path(account)
        else:
            print "Failed Delete: Not a File - ", self.build_path(account)

    #Search the password database for matches
    def find(self, search):
        search_tokens = search.split()
        #print "Tokens: ", search_tokens
        resuts = self.build_gpg_list(self.build_path(''), search_tokens)
        print resuts
        return resuts

    #Create a folder
    def createFolder(self, folder, path):
        physical_path = self.build_path(path)
        #print "Physical path: ", physical_path
        dir_list = self.build_dir(physical_path)
        #print dir_list
        if folder + "/" not in dir_list:
            if not physical_path.endswith("/"):
                physical_path += "/"
            physical_path += folder
            print physical_path
            os.makedirs(physical_path)
        else:
            print "!!Warning!! Folder already exists"

    #Searches the file for the given search tokens
    def search_file(self, file_name, search_tokens):
        for token in search_tokens:
            #print file_name, " => ", file_name.count(token)
            if file_name.count(token) > 0:
                return True
        return False

    #Builds a dictionary of the files that contain the search_tokens
    def build_gpg_list(self, path, search_tokens):
        rtn = {}
        #pulls the current
        stream = os.listdir(path)
        stream.sort()
        for x in stream:
            #Skip hiden files
            if not x.startswith("."):
                #checks if x is a file
                if not os.path.isdir(path + "/" + x):
                    if self.search_file(x, search_tokens):
                        file_name = x[:-4]
                        rtn[file_name] = path + '/' + x
                else:
                    #print "else -> " + path + "/" + x
                    tmp = self.build_gpg_list(path + "/" + x, search_tokens)
                    if tmp != {}:
                        rtn[x] = tmp
        return rtn

    #Builds a dictionary of the files that contain the search_tokens
    def build_gpg_tree(self, path):
        rtn = {}
        #pulls the current
        stream = os.listdir(path)
        stream.sort()
        for x in stream:
            #Skip hiden files
            if not x.startswith("."):
                #checks if x is a file
                if not os.path.isdir(path + "/" + x):
                    file_name = x[:-4]
                    rtn[file_name] = path + '/' + x
                else:
                    #print "else -> " + path + "/" + x
                    rtn[x] = self.build_gpg_tree(path + "/" + x)
        return rtn

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
        tmp = self.gpass_config.password_store
        if not child_path == '':
            tmp +=  '/' + child_path
        #print tmp
        return tmp
