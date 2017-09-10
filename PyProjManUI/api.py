# API Class, used as a middle layer between core classes and UI, Web App and external apps

from PyProjManCore.proj_man import ProjMan


class API:
    """PyProjMan API Object exposes internal commands used by the core object PyPRojMan as API Calls"""

    def __init__(self, project: ProjMan):
        """Initializes API object with a project"""
        self._project = project

