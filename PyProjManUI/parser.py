from pyparsing import ZeroOrMore, Regex
from PyProjManCore.proj_man import ProjMan
import json
import os

# This parser object should handle the following entities
# action
# object(s)
# parameters
# each verb objects and parameters are linked to an API call defined in the api.py module


class OpCode:
    """Used to systematically communicate with ProjMan"""
    def __init__(self, verb=None, parameters=None, feedback=None, error=None):
        """Made of:
        a verb
        list of objects
        list of literals
         """
        self._verb = verb
        self._inp_params = parameters
        self._feedback = feedback
        self._error = error

    @property
    def error(self):
        return self._error

    def __str__(self):
        ret = "Opcode Verb : [{}] Parameters:".format(self._verb)
        for par in self._inp_params:
            ret = ret + "{}, ".format(par)
        ret = ret + " Feedback : {}   Error : {}".format(self._feedback, self._error)
        return ret


def tokenizer(inp: str):
    """Slice input string into tokens"""
    parser = ZeroOrMore(Regex(r'\[[^]]*\]') | Regex(r'"[^"]*"') | Regex(r'[^ ]+'))
    tokens = []
    for token in parser.parseString(inp):
        tokens.append(token.replace('"','').replace("'",'').replace('[','').replace(']',''))
    return tokens


class PyProjManParser:
    """PyProjMan parser used by the text based UI to interact with PyProjMan API"""
    def __init__(self, project: ProjMan = None, config_file=None):
        """This should contact API object first, but for Alpha release, it will directly contact ProjMan"""
        # Load Parser Data
        try:
            if config_file is None:
                config_file = os.path.join(os.getcwd(), 'data', 'parser.json')
            with open(config_file) as parser_data_file:
                parser_data = json.load(parser_data_file)
            self._version = parser_data['Version']
            self._release = parser_data['Release']
            self._ignore_case = parser_data['IgnoreCase']
            raw_primatives = parser_data['Primitives']
            self._primatives = {}
            for k, v in raw_primatives.items():
                self._primatives[k] = int(v, 16)  # Evaluate Hex
            del raw_primatives
            self._verbs = parser_data['Verbs']
            self._parameters = parser_data['Parameters']
            self._decorators = parser_data['Decorators']
            raw_reply = parser_data['Reply']
            self._reply = {}
            for k, v in raw_reply.items():
                self._reply[int(k)] = v
            del raw_reply
            raw_err_codes = parser_data['ErrorCodes']
            self._error_codes = {}
            for k, v in raw_err_codes.items():
                self._error_codes[int(k)] = v
            del raw_err_codes
        except FileNotFoundError:
            print("Configuration file not found")

        # Load initial project
        if project is None:
            project = ProjMan()
        self._project = project

    def listen(self):
        """Listens to user input"""
        _active = True
        while _active:
            inp = input("PyProjMan > ")  # 1: read input from user : in a form of a string
            op_code = self.parse(inp)  # 2: pass input string to parse() function : get op code
            op_code = self.hook(op_code)  # 3: pass op code to hook() : get feedback as op code
            self.feed_back(op_code)  # 4: display feedback op code to user via feed_back()
            if op_code._verb == self._primatives['EXIT']:
                _active = False

    def parse(self, inp: str):
        """parse input string to call functions
        :returns op code mapped to function calls from ProjMan"""
        op_code = OpCode()
        # TODO:
        # 1: split string into a verb and rest of string
        tokens = tokenizer(inp)
        # 2: lookup verb in the _verbs dictionary, and place its numeric value
        if tokens[0].lower() in self._verbs:
            op_code = OpCode(verb=self._primatives[self._verbs[tokens[0].lower()]])
            op_code._inp_params = []
            for token in tokens[1:]:
                if token.upper() in self._primatives:
                    op_code._inp_params.append(self._primatives[token.upper()])
                else:
                    op_code._inp_params.append(token)
        else:
            op_code = OpCode(error=903) # Invalid Verb

        # 3: slice input string into tokens; keywords and literals
        # literals identified by double quotes, single quotes or square brackets surrounding them
        # 4: lookup non literal tokens and replace them with values from _objects and _decoration dictionary
        # 5: check for syntax maps
        # if all is ok, return op code object
        # otherwise, return a syntax error op code object
        return op_code

    def feed_back(self, op_code: OpCode):
        """Returns feedback from PyProjMan to end user
        :returns a string to user interface"""

        # Reverse lookup Op Code into text using the _reply dictionary, and construct feedback
        # this should return a string
        op_code._feedback = self.lookup_primative(op_code._verb)
        for param in op_code._inp_params:
            if isinstance(param, int):
                op_code._feedback = op_code._feedback + " {}".format(self.lookup_primative(param))
            else:
                op_code._feedback = op_code._feedback + " {}".format(param)
        print("{} : {}".format(self._error_codes[op_code._error], op_code._feedback))
        return op_code

    def hook(self, op_code):
        """what really interacts with ProjMan
        :argument op_code
        :returns op code """
        # TODO:
        # Lookup verb in a large switch statement, and make a call based on the numeric value,
        # passing objects, and literals as arguments
        # collect response, and convert it into op code, and return it to caller function
        # Create a Project

        if op_code._verb == self._primatives['CREATE'] and op_code._inp_params[0] == self._primatives['PROJECT']:
            self._project = ProjMan(name=op_code._inp_params[1])
            op_code._error=100
        elif op_code._verb == self._primatives['EXIT']:
            op_code._error=200
        else:
            op_code._error=901
        return op_code

    def lookup_primative(self, primative_value):
        if primative_value in self._primatives.values():
            for k,v in self._primatives.items():
                if v == primative_value:
                    return k
        return None
