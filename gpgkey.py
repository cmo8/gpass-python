#!/usr/bin/python

import gnupg
import StringIO
from subprocess import Popen, PIPE
from pprint import pprint

class GPGkey:
    def __init__(self, gpgbinary, gpghome, key):
        self.gpg = gnupg.GPG(gpgbinary, gpghome)
        self.key = key

    def list_public_keys(self):
        pub_key = self.gpg.list_keys()
        print 'Public Keys:'
        pprint(pub_key)

    def list_private_keys(self):
        pri_key = self.gpg.list_keys(True)
        print 'Private Keys:'
        pprint(pri_key)

    def encrypt(self, message_in, key=None):
        eKey = self.key
        if key != None:
            eKey = key
        encrypted_str = self.gpg.encrypt(message_in, eKey)
        return encrypted_str

    def decrypt(self, encrypted_str_in):
        plain_str = self.gpg.decrypt(encrypted_str_in)
        return plain_str

    def encrypt_to_file(self, message_in, filepath_out, key=None):
        encrypt_str = self.encrypt(message_in, key)
        with open(filepath_out, 'w') as f:
            f.write(str(encrypt_str))


    def decrypt_from_file(self, filepath_in, filepath_out=None):
        with open(filepath_in, 'rb') as f:
            plain_str = self.decrypt(f.read())
        if filepath_out != None:
            open(filepath_out, 'w').write(plain_str)
            plain_str = filepath_out
        return plain_str

def main():
    gpgbinary = '/usr/bin/gpg2'
    gpghome = '/home/cmo/.gnupg'
    gpgkey_id = 'cmo.uwp.2010@gmail.com'
    testgpg = '/home/cmo/.password-store/test.gpg'
    gpg = GPGkey(gpgbinary, gpghome, gpgkey_id)
    gpg.list_private_keys()
    gpg.list_public_keys()
    encrypt_str = gpg.encrypt("Test of lib", None, None)
    print "Encrypted String: ", encrypt_str
    decrypt_str = gpg.decrypt(str(encrypt_str))
    print "Decrypted String: ", decrypt_str
    file_plain =gpg.decrypt_from_file(testgpg)
    print "File Test.gpg: ", file_plain

if __name__ =='__main__':main()
