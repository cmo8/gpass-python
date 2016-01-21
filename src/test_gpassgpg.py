import unittest
import os
from gPassGPG import GPassGPG 

gpgbinary = '/usr/bin/gpg2'
gpghome   = os.getcwd() + '/gpg'

class Test_GPassGPG(unittest.TestCase):
    def setup(self):
        print('Creating GPG home...')
        os.mkdir(gpghome)
        print(gpghome)
        gpg = GPassGPG(gpgbinary, gpghome)
        return gpg

    def clean(self):
        os.system('rm -rf ' + gpghome)

    #def test___init__(self):
    #    print(self.gpghome)
    #    self.gpg = gnupg.GPG(gpgbinary, gpghome)

    def test_list_keys(self):
        #Test for no Keys
        gpg = self.setup()
        self.assertEqual(gpg.list_keys(), [])
        self.clean()
        #


    def test_list_public_keys(self):
        pass

    def test_list_private_keys(self):
        pass

    def test_encrypt(self):
        pass

    def test_decrypt(self):
        pass
        
    def test_encrypt_to_file(self):
        pass
        
    def test_decrypt_from_file(self):
        pass
        
    def test_get_key_by_fingerprint(self):
        pass
        
    def test_generate_key(self):
        pass


unittest.main()