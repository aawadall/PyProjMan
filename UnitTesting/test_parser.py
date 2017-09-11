from unittest import TestCase

import os

from PyProjManCore.proj_man import ProjMan
from PyProjManUI.parser import PyProjManParser


def helper_load_cfg_file():
    p = PyProjManParser()
    p.load_parser_data(os.path.join(os.getcwd(),  'test.json'))
    return p

class TestPyProjManParser(TestCase):
    """Test PyProjManParser"""
    def test_init(self):
        """Can we define a PyProjManParserobject?"""
        proj = ProjMan()
        p = PyProjManParser()
        self.assertIsInstance(p, PyProjManParser)

    def test_load_parser_data_version(self):
        """Can read Version from Config file"""
        p = helper_load_cfg_file()
        self.assertEqual('0.0.2',p._version)

    def test_load_parser_data_release(self):
        """Can read Release from Config file"""
        p = helper_load_cfg_file()
        self.assertEqual('alpha',p._release)

    def test_load_parser_data_ignore_case(self):
        self.fail()

    def test_load_parser_data_primitives(self):
        self.fail()

    def test_load_parser_data_verbs(self):
        self.fail()

    def test_load_parser_data_parameters(self):
        self.fail()

    def test_load_parser_data_decorators(self):
        self.fail()

    def test_load_parser_data_reply(self):
        self.fail()

    def test_load_parser_data_err_codes(self):
        self.fail()

    def test_listen(self):
        self.fail()

    def test_parse(self):
        self.fail()

    def test_feed_back(self):
        self.fail()

    def test_hook(self):
        self.fail()
