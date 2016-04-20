#!/usr/bin/python

import gnupg

class GPassGPG:
    #Constructor
    def __init__(self, gpgbinary, gpghome):
        self.gpg = gnupg.GPG(gpgbinary, gpghome)

    #List the GPG keys
    def list_keys(self, private_keys = False):
        rtn = []
        pub_key = self.gpg.list_keys(private_keys)
        for key in pub_key:
            rtn.append(key['uids'][0])
        return rtn

    #Displays a summery of all the public keys
    def list_public_keys(self):
        pub_key = []
        pub_key = self.gpg.list_keys()
        return pub_key

    #Displays a summery of all the private keys
    def list_private_keys(self):
        pri_key = []
        pri_key = self.gpg.list_keys(True)
        return pri_key

    def get_key_by_fingerprint(self, fingerprint):
        keys = self.gpg.list_keys()
        for key in keys:
            if str(key['fingerprint']) == fingerprint:
                return str(key['uids'][0])
        return ''

    #create GPG key
    def generate_key(self, name_real, name_email, passphrase):
        params = {"key_type": "RSA", "key_length": 2048, "name_real": name_real, "name_email": name_email, "passphrase": passphrase}
        input_data = self.gpg.gen_key_input(**params)
        fingerprint = self.gpg.gen_key(input_data)
        key_uid = self.get_key_by_fingerprint(str(fingerprint))
        #print("Fingerprint: ", str(fingerprint))
        #print("Key UID: ", str(key_uid))
        return str(key_uid)

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


