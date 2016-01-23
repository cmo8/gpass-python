'''import unittest
import os
from gPassGit import GPassGit

class Test_GPassGit(unittest.TestCase):
    def setup(self):
        os.mkdir('testcase')
        print(os.path + '/testcase')

    def cleanup(self):
        os.remove('testcase')

    def test___init__(self):
        #Test Repo exists
        self.setup()

        self.cleanup()
        #Test Repo does not exists
        self.setup()

        self.cleanup()
        return False
        
    def test_isRepoSet(self):
        gpassgit = setup()
        self.assertTrue()

    def test_init(self):
    	pass

    def test_add(self):
    	pass

    def test_commit(self):
        pass

    def test_auth(self):
        pass

    def test_push(self):
        pass

    def test_pull(self):
        pass

    def test_acp(self):
        pass

unittest.main()
'''