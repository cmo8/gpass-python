import unittest
import os
from gPassConfig import GPassConfig

class Test_GPassConfig(unittest.TestCase):
    def setup(self):
        cfg = GPassConfig()
        return cfg

    def test_save_config(self):
        cfg = self.setup()
        cfg.save_config()
        cfgl.get_config()
        if cfg.get_password_store() == cfgl.get_password_store() and cfg.get_gpgbinary() == cfgl.get_gpgbinary() and cfg.get_gpghome() == cfgl.get_gpghome() and cfg.get_pass_length() == cfgl.get_pass_length() and cfg.get_active_char_group() == cfgl.get_active_char_group():
            self.assertTrue(True)
        self.assertTrue(False)

    def test_load_config(self):
        cfg = self.setup()
        self.assertTrue(cfg.load_config())
        cfg.save_config()
        cfgl.load_config()
        if cfg.get_password_store() == cfgl.get_password_store() and cfg.get_gpgbinary() == cfgl.get_gpgbinary() and cfg.get_gpghome() == cfgl.get_gpghome() and cfg.get_pass_length() == cfgl.get_pass_length() and cfg.get_active_char_group() == cfgl.get_active_char_group():
            self.assertTrue(True)
        self.assertTrue(False)

    def test_get_config(self):
        self.assertTrue(True)

    def test_config_test(self):
        self.assertTrue(True)

    def test_set_password_store(self):
        self.assertTrue(True)

    def test_set_gpgbinary(self):
        self.assertTrue(True)

    def test_set_gpghome(self):
        self.assertTrue(True)

    def test_get_password_store(self):
        self.assertTrue(True)

    def test_get_gpgbinary(self):
        self.assertTrue(True)

    def test_get_gpghome(self):
        self.assertTrue(True)

    def test_check_gpgbinary(self):
        self.assertTrue(True)

    def test_check_gpghome(self):
        self.assertTrue(True)

    def test_check_password_store(self):
        self.assertTrue(True)

    def test_get_pass_length(self):
        self.assertTrue(True)

    def test_get_active_char_group(self):
        self.assertTrue(True)

unittest.main()