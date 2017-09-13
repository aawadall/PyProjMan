from datetime import datetime
from unittest import TestCase
from PyProjManCore.task import Task
from PyProjManCore.time_element import TimeElement


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
        """Define planned start date"""
        expected = datetime(year=2017, month=11, day=30)
        planned = TimeElement()
        planned.start = expected
        t = Task("Sample Task")
        t.planned = planned
        self.assertEqual(expected, t.planned.start)

    def test_actual_dates(self):
        """Define actual start date"""
        expected = datetime(year=2017, month=11, day=30)
        actual = TimeElement()
        actual.start = expected
        t = Task("Sample Task")
        t.actual = actual
        self.assertEqual(expected, t.actual.start)

    def test_prerequisites(self):
        """
        Create a list of tasks
        Create a single task
        Assign list of tasks to the single task
        """
        target = Task()
        prereqs = []
        for i in range(10):
            p = Task("Super-task {}".format(i))
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
            d = Task("Sub-task {}".format(i))
            dependants.append(d)
        target.dependants = dependants
        self.assertEqual(dependants, target.dependants)

    def test_completed(self):
        """Test Task completion percentage"""
        t = Task()
        expected = 0.5
        t.completed = expected
        self.assertEqual(expected, t.completed)
