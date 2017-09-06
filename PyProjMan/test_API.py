from unittest import TestCase

from PyProjMan.api import API
from PyProjMan.task import Task


class TestAPI(TestCase):
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

    # Searching
    def test_find_task_by_name(self):
        """Test searching for a task by its name"""
        self.fail("Not implemented")

    # Reporting
    def test_project_summary(self):
        """Test project statistics calculation"""
        self.fail("Not implemented")

    def test_alter_task_name(self):
        """Test changing task name"""
        self.fail("Not implemented")

    # Actual
    # Start
    def test_define_actual_start(self):
        """Test defining actual start date/time for a task"""
        self.fail("Not implemented")

    def test_calculated_actual_start(self):
        """Test calculated task's actual start from actual end and actual duration"""
        self.fail("Not implemented")

    # End
    def test_define_actual_end(self):
        """Test defining actual end date/time for a task"""
        self.fail("Not implemented")

    def test_calculated_actual_end(self):
        """Test calculated task's actual end from actual start and actual duration"""
        self.fail("Not implemented")

    # Duration
    def test_define_actual_duration(self):
        """Test defining actual task duration"""
        self.fail("Not implemented")

    def test_calculated_actual_duration(self):
        """Test calculated task's actual duration from actual start and actual end"""
        self.fail("Not implemented")

    # Planned
    # Start
    def test_define_planned_start(self):
        """Test defining planned start date/time for a task"""
        self.fail("Not implemented")

    def test_calculated_planned_start(self):
        """Test calculated task's planned start from planned end and planned duration"""
        self.fail("Not implemented")

    # End
    def test_define_planned_end(self):
        """Test defining planned end date/time for a task"""
        self.fail("Not implemented")

    def test_calculated_planned_end(self):
        """Test calculated task's planned end from planned start and planned duration"""
        self.fail("Not implemented")

    # Duration
    def test_define_planned_duration(self):
        """Test defining planned task duration"""
        self.fail("Not implemented")

    def test_calculated_planned_duration(self):
        """Test calculated task's planned duration from planned start and planned end"""
        self.fail("Not implemented")

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
