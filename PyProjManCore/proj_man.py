from PyProjManCore.task import Task


class ProjMan:
    """Project Manager Object, uses Tasks and Time Elements"""
    def __init__(self, root: Task = None, name = None):
        """
        Initialize a project, with minimum one task as root task
        :type root: object
        """
        self._root = root
        self._name = name

    @property
    def root(self):
        """Root Task of this project"""
        return self._root

    @property
    def name(self):
        """Name of a project"""
        return self._name

    def add_child(self, child):
        self._root.append_dependant(child)

    def add_parent(self, parent):
        self._root.append_prerequisite(parent)
        self._root = parent

    @classmethod
    def list_tasks(self):
        """List of All Tasks defined in a project starting from root to last task"""
        print("List Tasks ")
        result = self._root.list_children( [self.root])
        return result
