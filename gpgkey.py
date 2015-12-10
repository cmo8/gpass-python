#!/usr/bin/python

from subprocess import Popen, PIPE
import gnupg
from pprint import pprint

class GPGkey:
    def __init__(self, gpgbinary, gpghome, key):
        self.gpg = gnupg.GPG(gpgbinary, gpghome)
        self.key = key

    def list_pudlic_keys(self):
        pub_key = self.gpg.list_keys()
        print 'Public Keys:'
        pprint(pub_key)

    def list_private_keys(self):
        pri_key = self.gpg.list_keys(True)
        print 'Private Keys:'
        pprint(pri_key)

    def encrypt(self, message_in, filepath_out=None, key=None):
        print 'encrypt stud'

    def decrypt(self, message_in, filepath_out=None, key=None):
        print 'decrypt stud'

    def encrypt_to_file(self, message_in, filepath_out=None, key=None):
        print 'encrypt stud'

    def decrypt_from_file(self, filepath_in, filepath_out=None, key=None):
        print 'decrypt stud'

def main():
    gpgbinary = '/usr/bin/gpg2'
    gpghome = '/home/cmo/.gnupg'
    gpgkey_id = 'cmo.uwp.2010@gmail.com'
    gpg = GPGkey(gpgbinary, gpghome, gpgkey_id)
    gpg.list_private_keys()
    gpg.list_pudlic_keys()

if __name__ =='__main__':main()
