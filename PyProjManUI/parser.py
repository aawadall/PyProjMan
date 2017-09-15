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
        self._override_feedback = False

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
            raw_primitives = parser_data['Primitives']
            self._primitives = {}
            for k, v in raw_primitives.items():
                self._primitives[k] = int(v, 16)  # Evaluate Hex
            del raw_primitives
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
            self._help_strings = parser_data['HelpString']

            self._valid = True
        except FileNotFoundError:
            print("""
Fatal Error:
Configuration file not found
Exiting
""")
            self._valid = False

        # Load initial project
        if project is None:
            project = ProjMan()
        self._project = project

    def listen(self):
        """Listens to user input"""
        _active = True
        op_code = OpCode()

        while _active:
            inp = input("PyProjMan > ")  # 1: read input from user : in a form of a string
            op_code._override_feedback = False
            op_code = self.parse(inp)  # 2: pass input string to parse() function : get op code
            op_code = self.hook(op_code)  # 3: pass op code to hook() : get feedback as op code
            self.feed_back(op_code)  # 4: display feedback op code to user via feed_back()
            if op_code._verb == self._primitives['EXIT']:
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
            op_code = OpCode(verb=self._primitives[self._verbs[tokens[0].lower()]])
            op_code._inp_params = []
            for token in tokens[1:]:
                if token.lower() in self._parameters:
                    op_code._inp_params.append(self._primitives[self._parameters[token.lower()]])
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
        if not op_code._override_feedback:
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

        if op_code._verb == self._primitives['CREATE'] and op_code._inp_params[0] == self._primitives['PROJECT']:
            self._project = ProjMan(name=op_code._inp_params[1])
            op_code._error=100
        elif op_code._verb == self._primitives['EXIT']:
            op_code._error=200
        elif op_code._verb == self._primitives['MANUAL']:
            op_code = self.help(op_code)
        else:
            op_code._error=901
        return op_code

    def lookup_primative(self, primative_value):
        if primative_value in self._primitives.values():
            for k,v in self._primitives.items():
                if v == primative_value:
                    return k
        return None

    @property
    def valid(self):
        return self._valid

    @property
    def release(self):
        return self._release

    @property
    def version(self):
        return self._version

    def help(self, op_code):
        """Provides Help on how to use the CLI"""
        if len(op_code._inp_params) > 0:
            inquiry = op_code._inp_params[0]
            if isinstance(inquiry, int):
                if inquiry in self._primitives.values():
                    inquiry = self.lookup_primative(inquiry)

            # Lookup keywords
            # In verbs
            if inquiry in self._verbs.keys():
                inquiry = self._verbs[inquiry]

            # In Parameters
            if inquiry in self._parameters.keys():
                inquiry = self._parameters[inquiry]

            if inquiry in self._primitives.keys():
                op_code._feedback = "{} ({}) \n{}".format(op_code._inp_params[0],inquiry, self.help_primitive(inquiry))
            else:
                op_code._feedback = 'Unable to find keyword {}'.format(op_code._inp_params[0])
                op_code._error = 902
                op_code._override_feedback = True
                return op_code
        else:
            op_code._feedback = "PyProjMan version {} - {} release!".format(self.version, self.release)
            op_code._feedback = op_code._feedback + "\nList of keywords :"
            for verb_key, primitive_key in self._verbs.items():
                op_code._feedback = op_code._feedback  + "\n {} \t- \t{}".format(verb_key,self.help_primitive(primitive_key))
        op_code._error = 100
        op_code._override_feedback = True
        return op_code

    def help_primitive(self, prim):
        """Givin a primitive key, get help text"""
        return self._help_strings[prim]