# Entry point to the application
import os

from PyProjManUI.parser import PyProjManParser


def main(args=None):
    """PyProjMan, a commandline project management tool, with brains!"""
    print("Welcome to PyProjMan")
    p = PyProjManParser(config_file=os.path.join(os.getcwd(), 'parser.json'))
    if p.valid:
        print("""Release : {} - {}
A commandline project management tool
With Brains!""".format(p.version, p.release))
        if args is not None:
            p.parse(args)
        p.listen()


if __name__ == "__main__":
    main()
