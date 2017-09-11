from PyProjManCore.proj_man import ProjMan
import json
import os
from pprint import pprint
# This parser object should handle the following entities
# action
# object(s)
# parameters
# each verb objects and parameters are linked to an API call defined in the api.py module
class OpCode:
    """Used to systematically communicate with ProjMan"""
    def __init__(self, verb, parameters):
        """Made of:
        a verb
        list of objects
        list of literals
         """
        self._verb = verb
        self._inp_params = parameters
        self._feedback = []


class PyProjManParser:
    """PyProjMan parser used by the text based UI to interact with PyProjMan API"""
    def __init__(self, project: ProjMan = None):
        """This should contact API object first, but for Alpha release, it will directly contact ProjMan"""
        # Load Parser Data
        try:
            config_file = os.path.join(os.getcwd(), 'data', 'parser.json')
            self.load_parser_data(config_file)
        except FileNotFoundError:
            print("Configuration file not found")

        # Load initial project
        if project is None:
            project = ProjMan()
        self._project = project

    def load_parser_data(self, parser_config_file):
        """Load Parser Configuration from a file"""
        with open(parser_config_file) as parser_data_file:
            parser_data = json.load(parser_data_file)
        self._version = parser_data['Version']
        self._release = parser_data['Release']
        self._ignore_case = parser_data['IgnoreCase']
        raw_primatives = parser_data['Primitives']
        self._primatives = {}
        for k,v in raw_primatives.items():
            self._primatives[k] = int(v,16)
        del raw_primatives
        self._verbs = parser_data['Verbs']
        self._parameters = parser_data['Parameters']
        self._decorators = parser_data['Decorators']
        self._reply = parser_data['Reply']
        raw_err_codes = parser_data['ErrorCodes']
        self._error_codes = {}
        for k,v in raw_err_codes.items():
            self._error_codes[int(k)] = v
        del raw_err_codes

    def listen(self):
        """Listens to user input"""
        _active = True
        while _active:
            inp = input("PyProjMan > ")  # 1: read input from user : in a form of a string
            op_code = self.parse(inp)  # 2: pass input string to parse() function : get op code
            op_code = self.hook(op_code)  # 3: pass op code to hook() : get feedback as op code
            self.feed_back(op_code)  # 4: display feedback op code to user via feed_back()
        pass

    def parse(self, inp: str):
        """parse input string to call functions
        :returns op code mapped to function calls from ProjMan"""
        # TODO:
        # 1: split string into a verb and rest of string
        # 2: lookup verb in the _verbs dictionary, and place its numeric value
        # 3: slice input string into tokens; keywords and literals
        # literals identified by double quotes, single quotes or square brackets surrounding them
        # 4: lookup non literal tokens and replace them with values from _objects and _decoration dictionary
        # 5: check for syntax maps
        # if all is ok, return op code object
        # otherwise, return a syntax error op code object
        pass

    def feed_back(self, op_code: OpCode):
        """Returns feedback from PyProjMan to end user
        :returns a string to user interface"""
        # TODO:
        # Reverse lookup Op Code into text using the _reply dictionary, and construct feedback
        # this should return a string
        pass

    def hook(self, op_code):
        """what really interacts with ProjMan
        :argument op_code
        :returns op code """
        # TODO:
        # Lookup verb in a large switch statement, and make a call based on the numeric value,
        # passing objects, and literals as arguments
        # collect response, and convert it into op code, and return it to caller function
        pass

Proj = ProjMan()
par = PyProjManParser(Proj)