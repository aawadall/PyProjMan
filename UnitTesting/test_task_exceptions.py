from unittest import TestCase

from PyProjMan.task import Task


class TestTaskOperationsExceptions(TestCase):
    """Test Exceptions for Task operations"""
    def test_append_duplicate_prereq(self):
        """Test appending duplicate prerequisites to a task, it should be unique"""
        root = Task("Root Task")
        parent = Task("Parent Task")
        root.append_prerequisite(parent)
        root.append_prerequisite(parent)
        self.assertNotEqual(2, len(root.prerequisites))

    def test_cyclic_dependency(self):
        """
        Test case of a cyclic dependency, i.e. a Task depends on itself,
        or a task has both prerequisite and child the same
        """
        self.fail("Not implemented ")

    def test_append_duplicate_dep(self):
        """Test appending duplicate dependants to a task, it should be unique"""
        root = Task("Root Task")
        child = Task("Child Task")
        root.append_dependant(child)
        root.append_dependant(child)
        self.assertNotEqual(2, len(root.dependants))