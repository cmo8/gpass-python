#!/usr/bin/env python

from subprocess import Popen, PIPE
import gnupg
from pprint import pprint

class GPGkey:
    def __init__(self, gpghome, key):
        cmd_pub = "gpg --armor --export "
        #print cmd
        #parsed_cmd_pub = shlex.split(cmd_pub)
        proc_pub = Popen(cmd_pub, shell=True, stdout=PIPE, stderr=PIPE)
        pub_key, err_pub = proc_pub.communicate()
        cmd_prv = "gpg --armor --export "
        #print cmd
        #parsed_cmd_prv = shlex.split(cmd_prv)
        proc_prv = Popen(cmd_prv, shell=True, stdout=PIPE, stderr=PIPE)
        prv_key, err_prv = proc_prv.communicate()
        self.gpg = gnupg.GPG(gpghome)
        import_results = self.gpg.import_keys(pub_key + prv_key)
        pprint(import_results.results)
        #public_keys = self.gpg.list_keys()
        #pprint(public_keys)

def main():
    gpg = GPGkey('/home/cmo', 'cmo.uwp.2010@gmail.com')

if __name__ =='__main__':main()
