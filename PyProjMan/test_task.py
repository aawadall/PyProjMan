from unittest import TestCase
from PyProjMan.task import  Task
import datetime

class TestTask(TestCase):
    def test_calculate_date_from_duration(self):
        """Happy Path Date from duration"""
        baseline_date = datetime.datetime(year=2017,month=10,day=1,hour=10,minute=15)
        duration = datetime.timedelta(days=1, hours=1, minutes=10)
        expected = datetime.datetime(year=2017, month=10, day=2, hour=11, minute=25)
        self.assertEqual(Task.calculate_date_from_duration(date=baseline_date,duration=duration),expected)


    def test_calculate_date_from_duration_dur_exceptions(self):
        """Exception path,when duration is wrong data type"""
        baseline_date = datetime.datetime(year=2017, month=10, day=1, hour=10, minute=15)
        duration = 1

        self.assertEqual(None, Task.calculate_date_from_duration(date=baseline_date, duration=duration))

    def test_calculate_date_from_duration_date_exceptions(self):
        """Exception path,when date is wrong data type"""
        baseline_date = 1
        duration = datetime.timedelta(days=1, hours=1, minutes=10)

        self.assertEqual(None, Task.calculate_date_from_duration(date=baseline_date, duration=duration))

    def test_calculate_duration_from_date(self):
        """Happy Path, Calculating Duration from Start and End Dates"""
        baseline_date = datetime.datetime(year=2017,month=10,day=1,hour=10,minute=15)
        end_date = datetime.datetime(year=2017, month=10, day=2, hour=11, minute=25)
        expected = datetime.timedelta(days=1, hours=1, minutes=10)
        self.assertEqual(Task.calculate_duration_from_date(date1=baseline_date,date2=end_date),expected)

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
        """How to test UID?"""
        self.fail()

    def test_name(self):
        """Test Task Name Property Setter and Getter"""
        t = Task()
        expected = 'Task'
        t.name = expected
        self.assertEqual(t.name,expected, t.name)


    def test_prerequisites(self):
        self.fail()


    def test_append(self):
        self.fail()

    def test_extend(self):
        self.fail()

    def test_dependants(self):
        self.fail()


    def test_append(self):
        self.fail()

    def test_extend(self):
        self.fail()

    def test_planned_start(self):
        self.fail()


    def test_planned_end(self):
        self.fail()


    def test_planned_duration(self):
        self.fail()


    def test_actual_start(self):
        self.fail()


    def test_actual_end(self):
        self.fail()


    def test_actual_duration(self):
        self.fail()



    def test_completed(self):
        """Test Task completion percentage"""
        t = Task()
        expected = 0.5
        t.completed = expected
        self.assertEqual(expected,t.completed)
