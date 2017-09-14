## Entry point to the application
from PyProjManUI.parser import PyProjManParser


def main(args=None):
    """PyProjMan, a commandline project management tool, with brains!"""
    print("""Welcome to PyProjMan
    A commandline project management tool
    with brains!
    """)
    p = PyProjManParser()
    print("""Release:{}""".format(p._release))
    p.listen()

if __name__ == "__main__": main()