import os
from gPassGPG import GPassGPG
#from gPassGit import GPassGit
class GPass:

    #Creates a PyPass object
    def __init__(self, config):
        self.config = config
        self.gpg = GPassGPG(self.config.gpgbinary, self.config.gpghome)
        #self.git = GPassGit(self.config.get_password_store())

    def create(self, gpgkey, folderpath, setGit=False):
        os.mkdir(folderpath)
        self.config.set_password_store(folderpath)
        if setGit:
            print("Creating Git Repo...")
            #self.git.init(folderpath)
        self.add_gpg_key(gpgkey, self.config.get_password_store())

        #print('create')

    def add_gpg_key(self, gpgkey, folder):
        filepath = folder + '/.gpg-id'
        content = [];
        if os.path.isdir(filepath):
            with open(filepath, 'r') as f:
                content = f.readlines()
        #print(content)
        if not any(gpgkey in s for s in content):
            content.append(gpgkey)
        with open(filepath, 'w') as f:
            con_str = ""
            for key in content:
                con_str += key
                con_str += '\n'
            f.write(con_str)
        #if self.git.isRepoSet():
        #    self.git.acp(filepath, "Added GPG key to '" + folder + "' folder")
        #print('add_gpg_key')

    #Returns an unecrypted string of the selected file
    def account(self, account):
        out = self.gpg.decrypt_from_file(self.build_path(account))
        return str(out)

    #Inserts a GPG encrypted file into the password store
    def insert(self, account, message):
        if not message.endswith('\n'):
            message += '\n'
        keys = self.check_gpgkeys(account)
        msg = ""
        if os.path.isfile(self.build_path(account)):
            msg = "Inserted user account '" + account + "'"
        else:
            msg = "Updated user account '" + account + "'"
        out = self.gpg.encrypt_to_file(message, self.build_path(account), keys)
        #if self.git.isRepoSet():
        #    self.git.acp(self.build_path(account), msg)

    #Deletes the selected account
    def delete(self, account):
        if not os.path.isdir(self.build_path(account)):
            os.remove(self.build_path(account))
            print("Deleted: ", self.build_path(account))
        else:
            print("Failed Delete: Not a File - ", self.build_path(account))

    #Search the password database for matches
    def find(self, search):
        search_tokens = search.split()
        #print("Tokens: ", search_tokens)
        resuts = self.build_gpg_list(self.build_path(''), search_tokens)
        #print(resuts)
        return resuts

    #Create a folder
    def createFolder(self, folder, path):
        physical_path = self.build_path(path)
        #print("Physical path: ", physical_path)
        dir_list = self.build_dir(physical_path)
        #print(dir_list)
        if folder + "/" not in dir_list:
            if not physical_path.endswith("/"):
                physical_path += "/"
            physical_path += folder
            #print(physical_path)
            os.makedirs(physical_path)
        else:
            print("!!Warning!! Folder already exists")

    #Searches the file for the given search tokens
    def search_file(self, file_name, search_tokens):
        for token in search_tokens:
            #print(file_name, " => ", file_name.count(token))
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
                    #print("else -> " + path + "/" + x)
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
                    #print("else -> " + path + "/" + x)
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
                    #print("else -> " + path + "/" + x)
                    rtn.append(x + "/")
        rtn.sort()
        return rtn

    def gpg_id(self, path):
        gpgid = self.build_path(path) + '/.gpg-id'
        #print(gpgid)
        tmp = []
        if os.path.isfile(gpgid):
            with open(gpgid, 'r') as f:
                tmp = f.readlines()
        else:
            with open(self.config.get_password_store() + '/.gpg-id') as f:
                tmp = f.readlines()
        #print(tmp)
        rtn = []
        for a in tmp:
            if a.endswith("\n"):
                rtn.append(a[:-1])
            else:
                rtn.append(a)
        #print(rtn)
        return rtn

    def gpg_id_write(self, path, gpgid):
        gpgid_path = self.build_path(path) + '/.gpg-id'
        print("Writing..." + gpgid_path)
        with open(gpgid_path, 'w') as f:
            for key in gpgid:
                f.write(key[0] + '\n')

    #Returns an array of the items in the directory location
    def pass_array(self, child_path = ""):
        dir_items = self.build_dir(self.build_path(child_path))
        return dir_items

    #Concatinates the root password store path with the child path
    def build_path(self, child_path):
        tmp = self.config.password_store
        if not child_path == '':
            tmp +=  '/' + child_path
        #print(tmp)
        return tmp

    def check_gpgkeys(self, folderpath):
        tmp = []
        keys = []
        gpg_id = folderpath + '/.gpg-id'
        #print("GPG ID: " + gpg_id)
        if os.path.isfile(gpg_id):
            with open(gpg_id, 'r') as f:
                tmp = f.readlines()
        else:
            with open(self.config.password_store + '/.gpg-id', 'r') as f:
                tmp = f.readlines()
        for tp in tmp:
            keys.append(tp[:-1])
        #print("GPG Keys:")
        #print(keys)
        return keys
