from ..gpgkey import GPGkey

class TestGPGKey:
    def __init__(self):
        self.run()

    def run(self):
        gpgbinary = '/usr/bin/gpg2'
        gpghome = '/home/cmo/.gnupg'
        gpgkey_id = 'cmo.uwp.2010@gmail.com'
        gpg = GPGkey(gpgbinary, gpghome, gpgkey_id)
        gpg.list_private_keys()
        gpg.list_pudlic_keys()


