from PyProjManCore.task import Task


class ProjMan:
    """Project Manager Object, uses Tasks and Time Elements"""
    def __init__(self, root: Task):
        """
        Initialize a project, with minimum one task as root task
        :type root: object
        """
        _root = root