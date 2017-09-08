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

    def test_parent_child_upstream(self):
        """Test that defining a prerequisite implies defining the caller as a dependant"""
        self.fail("Not implemented")

    def test_parent_child_downstream(self):
        """Test that defining a dependant implies defining the caller as a prerequisite"""
        self.fail("Not implemented")

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

    def test_crawl_up(self):
        """Test Crawl Up a Task"""
        # Define a Task
        # Define 3 Layers of tasks
        # Assign each layer the layer over it as a prerequisite
        self.fail("Not implemented")

    def test_crawl_down(self):
        """Test Crawl Down a Task"""
        self.fail("Not implemented")
