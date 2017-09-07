from unittest import TestCase

from PyProjManCore.task import Task
from PyProjManUI.api import API


class TestAPIInit(TestCase):
    """Test Initialization related API Calls"""
    # Initialization
    def test_init_blank(self):
        """Test instantiating API object with no root Task"""
        api = API()
        self.assertIsNone(api.root, api.root)

    def test_init_existing(self):
        """Test instantiating API object with an existing root Task"""
        task = Task()
        task.name = "Root Task"
        api = API(task)
        self.assertEqual(task, api.root)


class TestAPITaskMgmt(TestCase):
    """Test Task Management API Calls"""
    # Task Management
    def test_create_root_task(self):
        """Test creating root task in an API object with no root task"""
        task = Task()
        task.name = "Root Task"

        api = API()
        api.root = task

        self.assertEqual(task, api.root)

    def test_create_root_task_existing(self):
        """Test creating root task in an API object with existing root task"""
        task = Task()
        task.name = "Root Task"

        api = API(task)

        task2 = Task()
        task2.name = "Second Root Task"

        api.root = task2

        self.assertTrue(api.root == task and api.root != task2)

    # Completed
    def test_completed_define(self):
        """Test defining a completed percentage of a task"""
        self.fail("Not implemented")

    def test_completed_increase(self):
        """Test increasing a completed percentage of a task"""
        self.fail("Not implemented")

    def test_completed_decrease(self):
        """Test decreasing a completed percentage of a task"""
        self.fail("Not implemented")

    # Assignee
    def test_assign_assignee(self):
        """Test defining assignee to a task"""
        self.fail("Not implemented")

    def test_un_assign_assignee(self):
        """Test un-assigning a task"""
        self.fail("Not implemented")


class TestAPILists(TestCase):
    """Test Lists related API Calls"""
    # Dependants & Prerequisites
    def test_adding_dependant_task(self):
        """Test appending a dependant task to root object"""
        task = Task()
        task.name = "Root Task"

        api = API(task)

        child = Task()
        child.name = "Child Task"

        api.add_dependant(child)

        self.assertIn(child, api.root.dependants)

    def test_adding_bad_dependant_task(self):
        """Test appending a dependant with type other than task to root object"""
        task = Task()
        task.name = "Root Task"

        api = API(task)

        child = 1

        api.add_dependant(child)

        self.assertNotIn(child, api.root.dependants)

    def test_adding_prerequisite_task(self):
        """Test appending a prerequisite task to root object"""
        task = Task()
        task.name = "Root Task"

        api = API(task)

        parent = Task()
        parent.name = "Child Task"

        api.add_prerequisite(parent)

        self.assertIn(parent, api.root.prerequisites)

    def test_adding_bad_prerequisite_task(self):
        """Test appending a bad prerequisite task to root object"""
        task = Task()
        task.name = "Root Task"

        api = API(task)

        parent = "Child Task"

        api.add_prerequisite(parent)

        self.assertNotIn(parent, api.root.prerequisites)

    def test_deleting_dependant_task(self):
        """Test deleting a dependant task"""
        self.fail("Not implemented")

    def test_deleting_prerequisite_task(self):
        """Test deleting a prerequisite task"""
        self.fail("Not implemented")

    def test_deleting_cascaded_dependants(self):
        """Test deleting a dependant task with dependants of its own"""
        self.fail("Not implemented")

    def test_deleting_cascaded_prerequisites(self):
        """Test deleting a prerequisite task with prerequisites of its own"""
        self.fail("Not implemented")


class TestAPISearch(TestCase):
    """Test Search Related API Calls"""
    # Searching
    def test_find_task_by_name(self):
        """Test searching for a task by its name"""
        self.fail("Not implemented")


class TestAPIReport(TestCase):
    """Test Reporting related API Calls"""
    # Reporting
    def test_project_summary(self):
        """Test project statistics calculation"""
        self.fail("Not implemented")

    def test_alter_task_name(self):
        """Test changing task name"""
        self.fail("Not implemented")


class TestAPITimings(TestCase):
    """Test Timings related API Calls"""
    def test_planned(self):
        """Test planned timings"""
        self.fail("Not implemented")

    def test_Actual(self):
        """Test actual timings"""
        self.fail("Not implemented")
