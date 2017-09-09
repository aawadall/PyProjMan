from PyProjManCore.task import Task


class ProjStats:
    """Project Statistics Object, used for reporting purposes"""
    def __init__(self, name = None):
        """empty object"""
        self._project_name = name
        self._first_task = None
        self._last_task = None
        self._task_count = 0
        self._project_duration = None
        self._list_tasks = []

    @property
    def name(self):
        return self._project_name

    @name.setter
    def name(self, value):
        self._project_name = value

    @property
    def first(self):
        return self._first_task

    @first.setter
    def first(self, value : Task ):
        self._first_task = value

    @property
    def last(self):
        return self._last_task

    @last.setter
    def last(self, value : Task):
        self._last_task = value

    @property
    def count(self):
        return self._task_count

    @count.setter
    def count(self, value):
        self._task_count = value

    @property
    def duration(self):
        return self._project_duration

    @duration.setter
    def duration(self, value):
        self._project_duration = value

    @property
    def tasks(self):
        return self._list_tasks

    @tasks.setter
    def tasks(self, value):
        self._list_tasks = value

    def append_task(self, value):
        self._list_tasks.append(value)

    def remove_task(self, value):
        while value in self._list_tasks:
            self._list_tasks.remove(value)
