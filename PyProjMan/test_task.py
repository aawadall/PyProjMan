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


    def test_calculate_date_from_duration_exceptions(self):
        """Exception path,when date or duration are wrong format"""
        self.fail()
    def test_calculate_duration_from_date(self):
        self.fail()

    def test_id(self):
        self.fail()

    def test_name(self):
        self.fail()

    def test_name(self):
        self.fail()

    def test_prerequisites(self):
        self.fail()

    def test_prerequisites(self):
        self.fail()

    def test_append(self):
        self.fail()

    def test_extend(self):
        self.fail()

    def test_dependants(self):
        self.fail()

    def test_dependants(self):
        self.fail()

    def test_append(self):
        self.fail()

    def test_extend(self):
        self.fail()

    def test_planned_start(self):
        self.fail()

    def test_planned_start(self):
        self.fail()

    def test_planned_end(self):
        self.fail()

    def test_planned_end(self):
        self.fail()

    def test_planned_duration(self):
        self.fail()

    def test_planned_duration(self):
        self.fail()

    def test_actual_start(self):
        self.fail()

    def test_actual_start(self):
        self.fail()

    def test_actual_end(self):
        self.fail()

    def test_actual_end(self):
        self.fail()

    def test_actual_duration(self):
        self.fail()

    def test_actual_duration(self):
        self.fail()

    def test_completed(self):
        self.fail()

    def test_completed(self):
        self.fail()
