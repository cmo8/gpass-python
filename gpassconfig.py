import os
from git import Repo

class GPassConfig:

    #Constructor
    def __init__(self):
        self.password_len = 25
        self.char_set = {'alpha'    : 'abcdefghijklmnopqurstuvwxyz',
                         'ALPHA'    : 'ABCDEFGHIJKLMNOPQURSTUVWXYZ',
                         'int'      : '0123456789',
                         'symbols'  : '!@#$%^&*()_-+={}|[]?><~`',
                         'ssymbols' : '!@#$&*?'}
        self.live_char_set = ['alpha', 'ALPHA', 'int', 'ssymbols']
        self.gpgbinary = '/usr/bin/gpg2'
        self.isgpgbinary = self.check_gpgbinary(self.gpgbinary)
        self.gpghome = os.environ['HOME'] + '/.gnupg'
        self.isgpghome = self.check_gpghome(self.gpghome)
        #self.gpghome = ''
        self.ispassword_store = False
        self.password_store = os.environ['HOME'] + '/.password-store'
        #self.password_store = ''
        self.isgpgkey = False
        self.gpgkey = ''
        self.git = False

    def load_config(self):
        if os.path.isfile(os.environ['HOME'] + '/.gpass.config'):
            self.get_config()
            self.isgpgbinary = self.check_gpgbinary(self.gpgbinary)
            self.isgpghome = self.check_gpghome(self.gpghome)
            self.ispassword_store = self.check_password_store(self.password_store)
            self.isgpgkey = self.check_gpgkey(self.gpgkey)
            if self.isgpgbinary and self.isgpghome and self.ispassword_store:# and self.isgpgkey:
                return True
        else:
            print('Warning: No Config file found')
        return False

    #Reads in the config file and stores the variables.
    def get_config(self):
        with open('gpass.config', 'r') as f:
            for line in f:
                if not line.startswith('#'):
                    conf = line.split(' = ')
                    print(conf)
                    if conf[0] == 'password_len':
                        self.password_len = conf[1][:-1]
                    elif conf[0] == 'char_set':
                        chset = conf[1].split(':')
                        self.char_set[chset[0]] = chset[1][:-1]
                    elif conf[0] == 'char_sets_to_use':
                        self.live_char_set = conf[1][:-1].split(', ')
                    elif conf[0] == 'gpgbinary':
                        self.gpgbinary = conf[1][:-1]
                    elif conf[0] == 'gpghome':
                        if conf[1].startswith('$HOME'):
                            self.gpghome = os.environ['HOME'] + conf[1][5:-1]
                        else:
                            self.gpghome = conf[1][:-1]
                    elif conf[0] == 'password_store':
                        if conf[1].startswith('$HOME'):
                            self.password_store = os.environ['HOME'] + conf[1][5:-1]
                        else:
                            self.password_store = conf[1][:-1]

                    elif conf[0] == 'gpgkey':
                        print("gpgKey: " + conf[1][:-1])
                        self.gpgkey = conf[1][:-1]

    #Test Function to display the current config
    def config_test(self):
        print("Password Length          : ", self.password_len)
        print("Character Sets           : ", self.char_set)
        print("Active Character Sets    : ", self.live_char_set)
        print("Default PGP Binary       : ", self.gpgbinary, self.isgpgbinary)
        print("Default PGP Home         : ", self.gpghome, self.isgpghome)
        print("Default Password Store   : ", self.password_store, self.ispassword_store)
        print("Default GPG key          : ", self.gpgkey, self.isgpgkey)

    def set_password_store(self, password_store_path):
        if self.check_password_store(password_store_path):
            self.password_store = password_store_path
            self.ispassword_store = True
            return self.ispassword_store
        return False

    def set_gpgbinary(self, gpgbinary):
        if self.check_gpgbinary(gpgbinary):
            self.gpgbinary = gpgbinary
            self.isgpgbinary = True
            return self.isgpgbinary
        return False

    def set_gpghome(self, gpghome):
        if self.check_gpghome(gpghome):
            self.gpghome = gpghome
            self.isgpghome = True
            return self.isgpghome
        return False

    def set_gpgkey(self, gpgkey):
        if self.check_gpgkey(gpgkey):
            self.gpgkey = gpgkey
            self.isgpgkey = True
            return self.isgpgkey
        return False

    def get_password_store(self):
        return self.password_store

    def get_gpgbinary(self):
        return self.gpgbinary

    def get_gpghome(self):
        return self.gpghome

    def get_gpgkey(self):
        return self.gpgkey

    #Write the current config to the file
    def save_config(self):
        with open('gpass.config', 'w') as f:
            f.write('###############################################################################\n')
            f.write('#                                Gpass Config                                 #\n')
            f.write('#                                                                             #\n')
            f.write('###############################################################################\n')
            f.write('#\n')
            f.write('#\n')
            f.write('#Lenght of password\n')
            f.write('password_len = ' + self.password_len + '\n')
            f.write('#\n')
            f.write('#Character Sets {char_set = Title:setOfCharacters}\n')
            for group in self.char_set:
                f.write('char_set = ' + group + ':' + self.char_set[group] +'\n')
            f.write('#\n')
            f.write('#default characters to use\n')
            f.write('char_sets_to_use = ' + ', '.join(self.live_char_set) + '\n')
            f.write('#\n')
            f.write('#GPG binary\n')
            f.write('gpgbinary = ' + self.gpgbinary + '\n')
            f.write('#\n')
            f.write('#GPG home\n')
            f.write('gpghome = ' + self.gpghome + '\n')
            f.write('#\n')
            f.write('#Default GPG key\n')
            f.write('gpgkey = ' + self.gpgkey + '\n')
            f.write('#\n')
            f.write('#Pass Password Store home\n')
            f.write('password_store = ' + self.password_store + '\n')

    # Checks if the gpgbinary exists
    def check_gpgbinary(self, gpgbinary):
        if gpgbinary == "":
            gpgbinary = self.gpgbinary
        if os.path.isfile(gpgbinary):
            return True
        return False
    # Checks if the gpg home folder exists
    def check_gpghome(self, gpghome):
        if gpghome == "":
            gpghome = self.gpghome
        if os.path.isdir(gpghome):
            return True
        return False
    # Checks if the gpg password store exists
    def check_password_store(self, password_store):
        if password_store == "":
            password_store = self.password_store
        if os.path.isdir(password_store):
            return True
        return False
    # Checks if the GPG key exists
    #TODO: check gpg key exists
    def check_gpgkey(self, gpgkey = ""):
        if gpgkey == "":
            gpgkey = self.gpgkey
        if os.path.isfile(gpgkey):
            return True
        return False
