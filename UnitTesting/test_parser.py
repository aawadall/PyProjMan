from unittest import TestCase

import os

from PyProjManCore.proj_man import ProjMan
from PyProjManUI.parser import PyProjManParser, OpCode


def helper_load_cfg_file():
    print(os.path.join('PyProjMan','UnitTesting', 'test.json'))
    #p = PyProjManParser(config_file=os.path.join(os.getcwd(), 'test.json'))
    p = PyProjManParser(config_file = os.path.join(os.getcwd(),'PyProjManUI','data', 'parser.json'))
    return p


class TestPyProjManParser(TestCase):
    """Test PyProjManParser"""
    def test_init(self):
        """Can we define a PyProjManParserobject?"""
        p = helper_load_cfg_file()
        self.assertIsInstance(p, PyProjManParser)

    def test_load_parser_data_version(self):
        """Can read Version from Config file"""
        p = helper_load_cfg_file()
        target = '0.0.3'
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
        self.assertEqual(target[key], p._primitives[key])

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
        key = 200
        value = 'Bye'
        target = {key: value}
        print(p._reply[key])
        self.assertEqual(target[key], p._reply[key])

    def test_load_parser_data_err_codes(self):
        """Can read Error Codes from Config file"""
        p = helper_load_cfg_file()
        key = 100
        value = 'Success'
        target = {key: value}
        self.assertEqual(target[key], p._error_codes[key])

    def test_parse_create_project_verb(self):
        """Parse input string of create project (Verb)"""
        p = helper_load_cfg_file()
        op_code = p.parse("CREATE PROJECT [Test Project]")
        target = p._primitives['CREATE']
        self.assertEqual(op_code._verb, target)

    def test_parse_create_project_parameters(self):
        """Parse input string of create project (Parameters)"""
        p = helper_load_cfg_file()
        op_code = p.parse("CREATE PROJECT [Test Project]")
        target = p._primitives['PROJECT']
        self.assertIn(target,op_code._inp_params)

    def test_parse_create_project_realization(self):
        """Parse input string of create project (Creates the project)"""
        p = helper_load_cfg_file()
        project_name = "Test Project"
        op_code = p.parse("CREATE PROJECT [{}]".format(project_name))
        print(op_code)
        op_code = p.hook(op_code)
        print(op_code)
        self.assertEqual(p._project.name, project_name)