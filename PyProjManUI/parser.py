from PyProjManCore.proj_man import ProjMan
# This parser object should handle the following entities
# action
# object(s)
# parameters
# each verb objects and parameters are linked to an API call defined in the api.py module
class OpCode:
    """Used to systematically communicate with ProjMan"""
    def __init__(self, verb, objects, literals):
        """Made of:
        a verb
        list of objects
        list of literals
         """
        self._verb = verb
        self._objects = objects
        self._literals = literals


class PyProjManParser:
    """PyProjMan parser used by the text based UI to interact with PyProjMan API"""
    def __init__(self, project: ProjMan):
        """This should contact API object first, but for Alpha release, it will directly contact ProjMan"""
        # TODO: Move this definition to a configuration file instead
        self._verbs = {
            'add':0,
            'adv':1,
            'advice':1,
            'assign':2,
            'create':3,
            'del':4,
            'delete':4,
            'dem':5,
            'demote':5,
            'est':6,
            'estimate':6,
            'exit':7,
            'help':8,
            'link':9,
            'list':10,
            'load':11,
            'open':11,
            'promote':12,
            'quit':7,
            'remove':4,
            'report':13,
            'save':14,
            'show':15,
            'summary':16,
            'sync':17,
            'synchronize':17
        }
        self._objects = {
            'best':0,
            'act':1,
            'actual':1,
            'dat':2,
            'date':2,
            'est':3,
            'estimated':3,
            'file':4,
            'planned':5,
            'proj':6,
            'project':6,
            'stat':7,
            'status':7,
            'task':8,
            'worst':9
        }
        self._decorators = {
            'on':1,
            'to':2,
            'from':3
        }

        self._project = project

    def listen(self):
        """Listens to user input"""
        # TODO: In a loop,
        # 1: read input from user : in a form of a string
        # 2: pass input string to parse() function : get op code
        # 3: pass op code to hook() : get feedback as op code
        # 4: display feedback op code to user via feed_back()
        pass

    def parse(self, input: str):
        """parse input string to call functions
        :returns op code mapped to function calls from ProjMan"""
        # TODO:
        # 1: split string into a verb and rest of string
        # 2: lookup verb in the _verbs dictionary, and place its numeric value
        # 3: search for literals (defined by single, double quotes or square brackets)
        # 4: place literals in the literals list
        # 5: parse the rest of the string into objects by looking up _objects dictionary
        # 6: check for syntax maps
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