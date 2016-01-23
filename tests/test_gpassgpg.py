import unittest
import os
from gPassGPG import GPassGPG 

gpgbinary = '/usr/bin/gpg2'
gpghome   = 'gpg'

class Test_GPassGPG(unittest.TestCase):
    def setup(self):
        print('Creating GPG home...')
        os.system('mkdir ' + gpghome)
        print('Selecting GPG Home...')
        gpg = GPassGPG(gpgbinary, gpghome)
        print('Returning GPG Home...')
        return gpg

    def clean(self):
        print('Removing GPG home...')
        os.system('rm -rf ' + gpghome)
        print('End Of Test Case')
        print('=========================================================')

    def test_empty_list_keys(self):
        os.system('rm -rf ' + gpghome)
        gpg = self.setup()
        print('self.assertEqual(gpg.list_keys(), [])')
        #Test for no public keys
        self.assertEqual(gpg.list_keys(), [])
        #Test for no Private keys
        print('self.assertEqual(gpg.list_keys(True), [])')
        self.assertEqual(gpg.list_keys(True), [])
        self.clean()

    def test_empty_list_public_keys(self):
        os.system('rm -rf ' + gpghome)
        gpg = self.setup()
        #Test for no public keys
        self.assertEqual(gpg.list_public_keys(), [])
        self.clean()

    def test_empty_list_private_keys(self):
        os.system('rm -rf ' + gpghome)
        gpg = self.setup()
        #Test for no Private keys
        self.assertEqual(gpg.list_private_keys(), [])
        self.clean()

    def test_generate_key(self):
        os.system('rm -rf ' + gpghome)
        gpg = self.setup()
        #Test for no Private keys
        name_real = "TestGPG"
        name_email = "testgpg@cmo.dev"
        passphrase = "testgpg"
        uid = name_real + ' <' + name_email + '>'
        self.assertEqual(gpg.generate_key(name_real, name_email, passphrase), uid)
        self.clean()

    def test_get_key_by_fingerprint(self):
        os.system('rm -rf ' + gpghome)
        gpg = self.setup()
        name_real = "TestGPG"
        name_email = "testgpg@cmo.dev"
        passphrase = "testgpg"
        uid = name_real + ' <' + name_email + '>'
        fingerprint = gpg.generate_key(name_real, name_email, passphrase)
        self.assertEqual(gpg.get_key_by_fingerprint(fingerprint), uid)
        self.clean()

    def test_encrypt(self):
        os.system('rm -rf ' + gpghome)
        gpg = self.setup()
        name_real = "TestGPG"
        name_email = "testgpg@cmo.dev"
        passphrase = "testgpg"
        msg = 'Test text for encrypting'
        key = gpg.get_key_by_fingerprint(gpg.generate_key(name_real, name_email, passphrase))
        crypto = gpg.encrypt(msg,[key])
        self.assertEqual(str(gpg.encrypt(msg,[key])), str(crypto))
        name_real = "TestGPG2"
        name_email = "testgpg2@cmo.dev"
        passphrase = "testgpg2"
        keyt = gpg.get_key_by_fingerprint(gpg.generate_key(name_real, name_email, passphrase))
        crypto = gpg.encrypt(msg,[key, keyt])
        self.assertEqual(str(gpg.encrypt(msg,[key, keyt])), str(crypto))
        self.clean()

    def test_decrypt(self):
        os.system('rm -rf ' + gpghome)
        gpg = self.setup()
        name_real = "TestGPG"
        name_email = "testgpg@cmo.dev"
        passphrase = "testgpg"
        msg = 'Test text for encrypting'
        key = gpg.get_key_by_fingerprint(gpg.generate_key(name_real, name_email, passphrase))
        crypto = gpg.encrypt(msg,[key])
        self.assertEqual(gpg.decrypt(crypto), msg)
        name_real = "TestGPG2"
        name_email = "testgpg2@cmo.dev"
        passphrase = "testgpg2"
        keyt = gpg.get_key_by_fingerprint(gpg.generate_key(name_real, name_email, passphrase))
        crypto = gpg.encrypt(msg,[key, keyt])
        self.assertEqual(gpg.decrypt(crypto), msg)
        self.clean()
        
    def test_encrypt_to_file(self):
        os.system('rm -rf ' + gpghome)
        gpg = self.setup()
        name_real = "TestGPG"
        name_email = "testgpg@cmo.dev"
        passphrase = "testgpg"
        msg = 'Test text for encrypting'
        filepath_out = 'test.pgp'
        key = gpg.get_key_by_fingerprint(gpg.generate_key(name_real, name_email, passphrase))
        crypto = gpg.encrypt(msg,[key])
        gpg.encrypt_to_file(msg,filepath_out, [key])
        data = ''
        with open(filepath_out, 'r') as f:
            data=f.read().replace('\n', '')
        self.assertEqual(str(data), str(crypto))
        os.system('rm ' + filepath_out)
        name_real = "TestGPG2"
        name_email = "testgpg2@cmo.dev"
        passphrase = "testgpg2"
        keyt = gpg.get_key_by_fingerprint(gpg.generate_key(name_real, name_email, passphrase))
        crypto = gpg.encrypt(msg,[key, keyt])
        gpg.encrypt_to_file(msg,filepath_out, [key, keyt])
        data = ''
        with open(filepath_out, 'r') as f:
            data=f.read().replace('\n', '')
        self.assertEqual(data, str(crypto))
        os.system('rm ' + filepath_out)
        self.clean()
        
    def test_decrypt_from_file(self):
        os.system('rm -rf ' + gpghome)
        gpg = self.setup()
        name_real = "TestGPG"
        name_email = "testgpg@cmo.dev"
        passphrase = "testgpg"
        msg = 'Test text for encrypting'
        filepath_out = 'test.pgp'
        key = gpg.get_key_by_fingerprint(gpg.generate_key(name_real, name_email, passphrase))
        gpg.encrypt_to_file(msg,filepath_out, [key])
        self.assertEqual(str(gpg.decrypt_from_file(filepath_out)), msg)
        os.system('rm ' + filepath_out)
        name_real = "TestGPG2"
        name_email = "testgpg2@cmo.dev"
        passphrase = "testgpg2"
        filepath_in = 'test.txt'
        keyt = gpg.get_key_by_fingerprint(gpg.generate_key(name_real, name_email, passphrase))
        crypto = gpg.encrypt(msg,[key, keyt])
        gpg.encrypt_to_file(msg,filepath_out, [key, keyt])
        gpg.decrypt_from_file(filepath_out, filepath_in)
        data = ''
        with open(filepath_in, 'r') as f:
            data=f.read().replace('\n', '')
        self.assertEqual(data, msg)
        os.system('rm ' + filepath_out)
        os.system('rm ' + filepath_in)
        self.clean()
        



unittest.main()