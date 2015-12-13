import os

class GPassConfig:
    def __init__(self):
        self.password_len = 0
        self.char_set = {}
        self.live_char_set = []
        self.gpgbinary = ''
        self.gpghome =''
        self.password_store = ''
        with open('pass.config', 'r') as f:
            for line in f:
                if !line.startswith('#'):
                    conf = line.split(' = ')
                    if conf[0] == 'password_len':
                        self.password_len = conf[1]
                    elif conf[0] == 'char_set':
                        chset = conf[1].split(':')
                        self.char_set{chset[0]} = chset[1]
                    elif conf[0] == 'char_sets_to_use':
                        self.live_char_set = conf[1].split(', ')
                    elif conf[0] == 'gpgbinary':
                        if conf[1].startswith('$HOME'):
                            home = os.environment('HOME')
                        self.gpgbinary =

        
