import  os

class GPassConfig:

    #Constructor
    def __init__(self):
        self.password_len = 0
        self.char_set = {}
        self.live_char_set = []
        self.gpgbinary = ''
        self.gpghome =''
        self.password_store = ''
        self.gpg_key = ''
        if os.path.isfile('gpass.config'):
            self.get_config()
            #self.config_test()
        else:
            print 'ERROR: No Config file found'

    #Reads in the config file and stores the variables.
    def get_config(self):
        with open('gpass.config', 'r') as f:
            for line in f:
                if not line.startswith('#'):
                    conf = line.split(' = ')
                    if conf[0] == 'password_len':
                        self.password_len = conf[1][:-1]
                    elif conf[0] == 'char_set':
                        chset = conf[1].split(':')
                        self.char_set[chset[0]] = chset[1][:-1]
                    elif conf[0] == 'char_sets_to_use':
                        self.live_char_set = conf[1].split(', ')
                    elif conf[0] == 'gpgbinary':
                        self.gpgbinary = conf[1][:-1]
                    elif conf[0] == 'gpghome':
                        if conf[1].startswith('$HOME'):
                            self.gpghome = os.environ['HOME'] + conf[1][5:-1]
                        else:
                            self.password_store = conf[1]
                    elif conf[0] == 'password_store':
                        if conf[1].startswith('$HOME'):
                            self.password_store = os.environ['HOME'] + conf[1][5:-1]
                        else:
                            self.password_store = conf[1]
                    elif conf[0] == 'gpgkey':
                        self.gpgkey = conf[1][:-1]

    #Test Function to display the current config
    def config_test(self):
        print "Password Length          : ", self.password_len
        print "Character Sets           : ", self.char_set
        print "Active Character Sets    : ", self.live_char_set
        print "Default PGP Binary       : ", self.gpgbinary
        print "Default PGP Home         : ", self.gpghome
        print "Default Password Store   : ", self.password_store
        print "Default GPG key          : ", self.gpg_key
