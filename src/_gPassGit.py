import os
from gittle import Gittle

class GPassGit:

    #Creates a Git object
    def __init__(self, repoPath):
        self.repoPath = repoPath
        self.repo = None
        if self.isRepoSet():
            self.repo = Gittle(self.repoPath)

    #Check For Git Repo
    def isRepoSet(self):
        if os.path.isfile(self.repoPath + '/.git/config'):
            return True
        return False

    def init(self, repoPath):
    	self.repo = Gittle.init(repoPath)
    	print("Created Repo")

    def add(self, filePath):
    	self.repo.stage([filePath])

    def commit(self, user, em, msg):
    	self.repo.commit(
            name=user,
            email=em,
            message=msg
        )

    # Authentication with RSA private key
    def auth(self, key):
        key_file = open(key)
        repo.auth(pkey=key_file)

    def push(self, key):
        self.auth(key)
        self.repo.push()

    def pull(self, key):
        self.auth(key)
        self.repo.pull()

    def acp(self, filepath, user, em, msg):
    	self.add(filepath)
    	self.commit(user, em, msg)
    	self.push(key)
        