from unittest import TestCase

from PyProjManCore.task import Task


class TestTaskOperationsHappyPath(TestCase):
    """Test Basic Operations of a task, in the happy path"""
    def test_append_prereq(self):
        """
        Create a Task
        Create another task and append it to prerequisites of first task
        """
        target = Task()
        prereq = Task()
        target.prerequisites.append(prereq)
        self.assertIn(prereq, target.prerequisites)

    def test_append_dependants(self):
        """
        Create a Task
        Create a second task
        Append second task to first task's list of dependants
        """
        target = Task()
        dep = Task()
        target.append_dependant(dep)
        self.assertIn(dep, target.dependants)
