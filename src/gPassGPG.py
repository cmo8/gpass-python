#!/usr/bin/python

import gnupg
#import StringIO
#from subprocess import Popen, PIPE
#from pprint import pprint

class GPassGPG:
    #Constructor
    def __init__(self, gpgbinary, gpghome):
        self.gpg = gnupg.GPG(gpgbinary, gpghome)

    #List the GPG keys
    def list_keys(self, private_keys = False):
        rtn = []
        pub_key = self.gpg.list_keys(private_keys)
        for key in pub_key:
            #print("KeyID:", type(key['keyid']))
            rtn.append(key['uids'][0])
        return rtn

    #Displays a summery of all the public keys
    def list_public_keys(self):
        pub_key = self.gpg.list_keys()
        #print('Public Keys:')
        #pprint(pub_key)

    #Displays a summery of all the private keys
    def list_private_keys(self):
        pri_key = self.gpg.list_keys(True)
        #print('Private Keys:')
        #pprint(pri_key)

    #Uses the default public key to encrypt the message unless otherwise stated
    def encrypt(self, message_in, keys):
        encrypted_str = self.gpg.encrypt(message_in, keys)
        return encrypted_str

    #Decrypts the encrypted message with the private key
    def decrypt(self, encrypted_str_in):
        plain_str = self.gpg.decrypt(encrypted_str_in)
        return plain_str

    #Encrypts a string and writes it to a specified file
    def encrypt_to_file(self, message_in, filepath_out, keys):
        encrypt_str = self.encrypt(message_in, keys)
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

    #create GPG key
    def generate_key(self, name_real, name_email, passphrase):
        params = {"key_type": "RSA", "key_length": 2048, "name_comment": "GPG Key Generated by gPass.", "name_real": name_real, "name_email": name_email, "passphrase": passphrase}
        input_data = self.gpg.gen_key_input(**params)
        key = self.gpg.gen_key(input_data)
        #print("Gen Key:", key)