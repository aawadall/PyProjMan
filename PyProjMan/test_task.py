
from unittest import TestCase
from PyProjMan.task import Task


class TestTaskParameters(TestCase):
    """Test Fields of Task Object"""
    def test_id(self):
        """Check if Task ID has UUID Version 4"""
        t = Task()
        expected = 4
        self.assertEqual(expected, t.id.version)

    def test_name(self):
        """Test Task Name Property Setter and Getter"""
        expected = 'Task'
        t = Task(expected)
        t.name = expected
        self.assertEqual(t.name, expected, t.name)

    def test_planned_dates(self):
        self.fail("Not implemented")

    def test_actual_dates(self):
        self.fail("Not implemented")

    def test_prerequisites(self):
        """
        Create a list of tasks
        Create a single task
        Assign list of tasks to the single task
        """
        target = Task()
        prereqs = []
        for i in range(10):
            p = Task()
            prereqs.append(p)
        target.prerequisites = prereqs

        self.assertEqual(prereqs, target.prerequisites)

    def test_dependants(self):
        """
        Create a task
        Create a set of tasks
        set set of tasks as dependants of the first task
        """
        target = Task()
        dependants = []
        for i in range(10):
            d = Task()
            dependants.append(d)
        target.dependants = dependants
        self.assertEqual(dependants, target.dependants)

    def test_completed(self):
        """Test Task completion percentage"""
        t = Task()
        expected = 0.5
        t.completed = expected
        self.assertEqual(expected, t.completed)


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
