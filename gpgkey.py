#!/usr/bin/python

import gnupg
import StringIO
from subprocess import Popen, PIPE
from pprint import pprint

class GPGkey:
    #Constructor
    def __init__(self, gpgbinary, gpghome):
        self.gpg = gnupg.GPG(gpgbinary, gpghome)

    #Set the Default Key
    def set_default_key(key):
        self.key = key

    def list_keys(self):
        rtn = {}
        pub_key = self.gpg.list_keys()
        for key in pub_key:
            #print "KeyID:", type(key['keyid'])
            rtn[key['keyid']] = key['uids'][0]
        return rtn

    #Displays a summery of all the public keys
    def list_public_keys(self):
        pub_key = self.gpg.list_keys()
        print 'Public Keys:'
        pprint(pub_key)

    #Displays a summery of all the private keys
    def list_private_keys(self):
        pri_key = self.gpg.list_keys(True)
        print 'Private Keys:'
        pprint(pri_key)

    #Uses the default public key to encrypt the message unless otherwise stated
    def encrypt(self, message_in, key=None):
        eKey = self.key
        if key != None:
            eKey = key
        encrypted_str = self.gpg.encrypt(message_in, eKey)
        return encrypted_str

    #Decrypts the encrypted message with the private key
    def decrypt(self, encrypted_str_in):
        plain_str = self.gpg.decrypt(encrypted_str_in)
        return plain_str

    #Encrypts a string and writes it to a specified file
    def encrypt_to_file(self, message_in, filepath_out, key=None):
        encrypt_str = self.encrypt(message_in, key)
        with open(filepath_out, 'w') as f:
            f.write(str(encrypt_str))

    #Decrypts the contents of a file and either writes it out to a file or
    #returns the plain text
    def decrypt_from_file(self, filepath_in, filepath_out=None):
        with open(filepath_in, 'rb') as f:
            plain_str = self.decrypt(f.read())
        if filepath_out != None:
            open(filepath_out, 'w').write(plain_str)
            plain_str = filepath_out
        return plain_str

