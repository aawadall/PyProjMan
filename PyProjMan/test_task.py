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

    def test_append_duplicate_prereq(self):
        """Test appending duplicate prerequisites to a task, it should be unique"""
        self.fail("Not implemented")

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

    def test_cyclic_dependencay(self):
        """Test case of a cyclic dependency, i.e. a Task depends on itself, or a task has both prerequisite and child the same"""
        self.fail("Not implemented ")

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
        target.dependants.append(dep)
        self.assertIn(dep, target.dependants)

    def test_append_duplicate_dep(self):
        """Test appending duplicate dependants to a task, it should be unique"""
        root = Task("Root Task")
        child = Task("Child Task")
        root.dependants.append(child)
        root.dependants.append(child)
        self.assertNotEqual(2,root.dependants.__len__())

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

    def test_planned_end_from_others(self):
        """Calculate Planned End Date from Start Date and Duration"""
        t = Task()
        start    = datetime.datetime(year=2017, month=10, day=1, hour=10, minute=15)
        end      = datetime.datetime(year=2017, month=10, day=2, hour=11, minute=25)
        duration = datetime.timedelta(days=1, hours=1, minutes=10)
        t.planned_start = start
        t.planned_duration = duration
        self.assertEqual(end, t.planned_end)

    def test_planned_duration_from_others(self):
        """Calculate Planned Duration from Start Date and End Date"""
        t = Task()
        start    = datetime.datetime(year=2017, month=10, day=1, hour=10, minute=15)
        end      = datetime.datetime(year=2017, month=10, day=2, hour=11, minute=25)
        duration = datetime.timedelta(days=1, hours=1, minutes=10)
        t.planned_start = start
        t.planned_end   = end
        self.assertEqual(duration, t.planned_duration)

    def test_planned_start_from_others(self):
        """Calculate Planned Start Date from End Date and Duration"""
        t = Task()
        start    = datetime.datetime(year=2017, month=10, day=1, hour=10, minute=15)
        end      = datetime.datetime(year=2017, month=10, day=2, hour=11, minute=25)
        duration = datetime.timedelta(days=1, hours=1, minutes=10)
        t.planned_end = end
        t.planned_duration = duration
        self.assertEqual(start, t.planned_start)

    def test_actual_end_from_others(self):
        """Calculate Actual End Date from Start Date and Duration"""
        t = Task()
        start    = datetime.datetime(year=2017, month=10, day=1, hour=10, minute=15)
        end      = datetime.datetime(year=2017, month=10, day=2, hour=11, minute=25)
        duration = datetime.timedelta(days=1, hours=1, minutes=10)
        t.actual_start = start
        t.actual_duration = duration
        self.assertEqual(end, t.actual_end)

    def test_actual_duration_from_others(self):
        """Calculate Actual Duration  from Start Date and End Date"""
        t = Task()
        start    = datetime.datetime(year=2017, month=10, day=1, hour=10, minute=15)
        end      = datetime.datetime(year=2017, month=10, day=2, hour=11, minute=25)
        duration = datetime.timedelta(days=1, hours=1, minutes=10)
        t.actual_start = start
        t.actual_end = end
        self.assertEqual(duration, t.actual_duration)

    def test_actual_start_from_others(self):
        """Calculate Actual Start Date from End Date and Duration"""
        t = Task()
        start    = datetime.datetime(year=2017, month=10, day=1, hour=10, minute=15)
        end      = datetime.datetime(year=2017, month=10, day=2, hour=11, minute=25)
        duration = datetime.timedelta(days=1, hours=1, minutes=10)
        t.actual_end = end
        t.actual_duration = duration
        self.assertEqual(start, t.actual_start)

    def test_crawl_up(self):
        """Test Crawl Up a Task"""
        # Define a Task
        root = Task("Root Task")

        # Define 3 Layers of tasks
        # Layer 1
        l1a = Task("Prerequisite a, Layer 1")
        l1b = Task("Prerequisite b, Layer 1")
        root.prerequisites.append(l1a)
        root.prerequisites.append(l1b)
        # Layer 2
        l2a = Task("Prerequisite a, Layer 2")
        l2b = Task("Prerequisite b, Layer 2")
        l1a.prerequisites.append(l2a)
        l1a.prerequisites.append(l2b)
        l2c = Task("Prerequisite c, Layer 2")
        l2d = Task("Prerequisite d, Layer 2")
        l1b.prerequisites.append(l2c)
        l1b.prerequisites.append(l2d)
        # Layer 3
        l3a = Task("Prerequisite a, Layer 3")
        l2a.prerequisites.append(l3a)
        l2b.prerequisites.append(l3a)
        l3b = Task("Prerequisite b, Layer 3")
        l2a.prerequisites.append(l3b)
        # Assign each layer the layer over it as a prerequisite

        c_up = root.crawl_up()

        self.assertIn(l1a,c_up)
        self.assertIn(l1b,c_up)
        self.assertIn(l2a,c_up)
        self.assertIn(l2b,c_up)
        self.assertIn(l2c,c_up)
        self.assertIn(l2d,c_up)
        self.assertIn(l3a,c_up)
        self.assertIn(l3b,c_up)

    def test_crawl_down(self):
        """Test Crawl Down a Task"""
        self.fail("Not implemented")

