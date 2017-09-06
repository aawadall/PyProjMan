# API Class, used as a middle layer between core classes and UI, Web App and external apps
from PyProjMan.task import Task


class API:
    """
    API Class, is used as a middle layer between core classes and external world,
    including Text based UI, Web App, and external systems
    """
    def __init__(self, root: Task=None):
        """Creates an API instance for the root task
        :type root: Task
        :param root:
        """
        self._root = root

    @property
    def root(self):
        """Root Task"""
        return self._root

    @root.setter
    def root(self, value):
        """Set Root if not defined"""
        if self._root is None and isinstance(value, Task):
            self._root = value

    def add_dependant(self, child):
        """Adds a dependant to root"""
        if self._root is not None and isinstance(child, Task):
            self._root.dependants.append(child)

    def add_prerequisite(self, parent):
        """Add a prerequisite to root"""
        if self._root is not None and isinstance(parent, Task):
            self._root.prerequisites.append(parent)
