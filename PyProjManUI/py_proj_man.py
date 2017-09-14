# Entry point to the application
from PyProjManUI.parser import PyProjManParser


def main(args=None):
    """PyProjMan, a commandline project management tool, with brains!"""
    p = PyProjManParser()
    print("""
Welcome to PyProjMan 
Release : {} - {}
A commandline project management tool
With Brains!
    """.format(p._version, p._release))
    if args is not None:
        p.parse(args)
    p.listen()

if __name__ == "__main__": main()