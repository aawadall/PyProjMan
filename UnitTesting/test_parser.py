from unittest import TestCase

import os

from PyProjManCore.proj_man import ProjMan
from PyProjManUI.parser import PyProjManParser


def helper_load_cfg_file():
    p = PyProjManParser(config_file= os.path.join('test.json'))
    #p.load_parser_data(os.path.join('test.json'))
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
        target = '0.0.2'
        self.assertEqual(target,p._version)

    def test_load_parser_data_release(self):
        """Can read Release from Config file"""
        p = helper_load_cfg_file()
        target = 'alpha'
        self.assertEqual(target,p._release)

    def test_load_parser_data_ignore_case(self):
        """Can read Ignore Case from Config file"""
        p = helper_load_cfg_file()
        target = True
        self.assertEqual(target, p._ignore_case)

    def test_load_parser_data_primitives(self):
        """Can read Primitives from Config file"""
        p = helper_load_cfg_file()
        target = {"ADD": 256}
        key = 'ADD'
        value = 256
        target = {key: value}
        self.assertEqual(target[key], p._primatives[key])


    def test_load_parser_data_verbs(self):
        """Can read Verbs from Config file"""
        p = helper_load_cfg_file()
        target = {"add": "ADD"}
        key = 'add'
        value = 'ADD'
        target = {key: value}
        self.assertEqual(target[key], p._verbs[key])

    def test_load_parser_data_parameters(self):
        """Can read Parameters from Config file"""
        p = helper_load_cfg_file()
        key = 'best'
        value = 'BEST'
        target = {key: value}
        self.assertEqual(target[key], p._parameters[key])


    def test_load_parser_data_decorators(self):
        """Can read Decorators from Config file"""
        p = helper_load_cfg_file()
        key = 'on'
        value = 'ON'
        target = {key: value}
        self.assertEqual(target[key], p._decorators[key])

    def test_load_parser_data_reply(self):
        """Can read Reply from Config file"""
        p = helper_load_cfg_file()
        key = 'SUCCESS'
        value = 'Success'
        target = {key: value}
        self.assertEqual(target[key], p._reply[key])

    def test_load_parser_data_err_codes(self):
        """Can read Error Codes from Config file"""
        p = helper_load_cfg_file()
        key = 100
        value = 'Success'
        target = {key: value}
        self.assertEqual(target[key], p._error_codes[key])
