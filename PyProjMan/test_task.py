import uuid
from unittest import TestCase
from PyProjMan.task import Task
import uuid
import datetime


class TestTask(TestCase):
    def test_calculate_end_date(self):
        """Happy Path Date from duration"""
        baseline_date = datetime.datetime(year=2017, month=10, day=1, hour=10, minute=15)
        duration = datetime.timedelta(days=1, hours=1, minutes=10)
        expected = datetime.datetime(year=2017, month=10, day=2, hour=11, minute=25)
        self.assertEqual(Task.calculate_end_date(baseline_date, duration=duration), expected)

    def test_calculate_end_date_dur_exceptions(self):
        """Exception path,when duration is wrong data type"""
        baseline_date = datetime.datetime(year=2017, month=10, day=1, hour=10, minute=15)
        duration = 1

        self.assertEqual(None, Task.calculate_end_date(baseline_date, duration=duration))

    def test_calculate_end_date_date_exceptions(self):
        """Exception path,when date is wrong data type"""
        baseline_date = 1
        duration = datetime.timedelta(days=1, hours=1, minutes=10)

        self.assertEqual(None, Task.calculate_end_date(baseline_date, duration=duration))

    def test_calculate_duration_from_date(self):
        """Happy Path, Calculating Duration from Start and End Dates"""
        baseline_date = datetime.datetime(year=2017, month=10, day=1, hour=10, minute=15)
        end_date = datetime.datetime(year=2017, month=10, day=2, hour=11, minute=25)
        expected = datetime.timedelta(days=1, hours=1, minutes=10)
        self.assertEqual(Task.calculate_duration_from_date(date1=baseline_date, date2=end_date), expected)

    def test_calculate_duration_from_date_ex_type_1_err(self):
        """Exception Path, First Argument, wrong data type"""
        baseline_date = 1
        end_date = datetime.datetime(year=2017, month=10, day=2, hour=11, minute=25)
        self.assertEqual(None, Task.calculate_duration_from_date(date1=baseline_date, date2=end_date))

    def test_calculate_duration_from_date_ex_type_2_err(self):
        """Exception Path, Second Argument, wrong data type"""
        baseline_date = datetime.datetime(year=2017, month=10, day=2, hour=11, minute=25)
        end_date = 1
        self.assertEqual(None, Task.calculate_duration_from_date(date1=baseline_date, date2=end_date))

    def test_calculate_duration_from_date_ex_date_2_less_t_date_1(self):
        """Exception Path, Second date smaller than first date"""
        baseline_date = datetime.datetime(year=2017, month=10, day=2, hour=11, minute=25)
        end_date = datetime.datetime(year=2017, month=10, day=1, hour=10, minute=15)

        self.assertEqual(Task.calculate_duration_from_date(date1=baseline_date, date2=end_date), None)

    def test_id(self):
        """Check if Task ID has UUID Version 4"""
        t = Task()
        expected = 4
        self.assertEqual(expected, t.id.version)

    def test_name(self):
        """Test Task Name Property Setter and Getter"""
        t = Task()
        expected = 'Task'
        t.name = expected
        self.assertEqual(t.name, expected, t.name)

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

    def test_append_prereq(self):
        """
        Create a Task
        Create another task and append it to prerequisites of first task
        """
        target = Task()
        prereq = Task()
        target.prerequisites.append(prereq)
        self.assertIn(prereq, target.prerequisites)

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

    def test_append_dependants(self):
        """
        Create a Task
        Create a second task
        Append second task to first task's list of dependants
        """
        target = Task()
        dep = Task()
        target.dependants.append(dep)
        self.assertIn(dep, target.dependants)

    def test_planned_start(self):
        """Create a task, define a _date/time, assign it to planned start _date"""
        target = Task()
        _date = datetime.datetime(year=2017, month=10, day=1, hour=10, minute=15)
        target.planned_start = _date
        self.assertEqual(target.planned_start, _date)

    def test_planned_end(self):
        """Create a task, define a date/time, assign it to planned end date"""
        target = Task()
        _date = datetime.datetime(year=2017, month=10, day=1, hour=10, minute=15)
        target.planned_end = _date
        self.assertEqual(target.planned_end, _date)

    def test_planned_duration(self):
        """Create a task, define duration, assign to planned duration"""
        target = Task()
        duration = datetime.timedelta(days=1, hours=1, minutes=10)
        target.planned_duration = duration
        self.assertEqual(target.planned_duration, duration)

    def test_actual_start(self):
        """Create a task, define a _date/time, assign it to actual start _date"""
        target = Task()
        _date = datetime.datetime(year=2017, month=10, day=1, hour=10, minute=15)
        target.actual_start = _date
        self.assertEqual(target.actual_start, _date)

    def test_actual_end(self):
        """Create a task, define a date/time, assign it to actual end date"""
        target = Task()
        _date = datetime.datetime(year=2017, month=10, day=1, hour=10, minute=15)
        target.actual_end = _date
        self.assertEqual(target.actual_end, _date)

    def test_actual_duration(self):
        """Create a task, define duration, assign to actual duration"""
        target = Task()
        duration = datetime.timedelta(days=1, hours=1, minutes=10)
        target.actual_duration = duration
        self.assertEqual(target.actual_duration, duration)

    def test_completed(self):
        """Test Task completion percentage"""
        t = Task()
        expected = 0.5
        t.completed = expected
        self.assertEqual(expected, t.completed)

        # def test_report(self):
        #     """Create a set of tasks, link them, assign data, and report it"""
        #     self.fail("Not implemented yet")

        # def test_factory_method(self):
        #     """Create tasks using a static factory method"""
        #     self.fail("Not implemented yet ")
        #
        # def test_t_ui(self):
        #     """User Interface, using text"""
        #     self.fail("Not Implemented Yet")



    def test_calculate_start_date(self):
        """Happy Path Date from duration"""
        expected = datetime.datetime(year=2017, month=10, day=1, hour=10, minute=15)
        duration = datetime.timedelta(days=1, hours=1, minutes=10)
        baseline_date = datetime.datetime(year=2017, month=10, day=2, hour=11, minute=25)
        self.assertEqual(Task.calculate_start_date(baseline_date, duration=duration), expected)

    def test_calculate_start_date_dur_exceptions(self):
        """Exception path,when duration is wrong data type"""
        baseline_date = datetime.datetime(year=2017, month=10, day=1, hour=10, minute=15)
        duration = 1

        self.assertEqual(None, Task.calculate_start_date(baseline_date, duration=duration))

    def test_calculate_start_date_date_exceptions(self):
        """Exception path,when date is wrong data type"""
        baseline_date = 1
        duration = datetime.timedelta(days=1, hours=1, minutes=10)

        self.assertEqual(None, Task.calculate_start_date(baseline_date, duration=duration))
