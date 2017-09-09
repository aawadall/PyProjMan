from datetime import timedelta
from unittest import TestCase

from PyProjManCore.proj_stats import ProjStats
from PyProjManCore.task import Task


class TestProjStats(TestCase):
    def test_init(self):
        stat = ProjStats()
        self.assertIsInstance(stat, ProjStats)

    def test_name_constructor(self):
        name = "Project Name"
        stat = ProjStats(name)
        self.assertEqual(name, stat.name)

    def test_name_attribute(self):
        name = "Project Name"
        stat = ProjStats()
        stat.name = name
        self.assertEqual(name, stat.name)

    def test_first(self):
        stat = ProjStats()
        first = Task("First")
        stat.first = first
        self.assertEqual(first, stat.first)

    def test_last(self):
        stat = ProjStats()
        last = Task("Last")
        stat.first = last
        self.assertEqual(last, stat.first)

    def test_count(self):
        stat = ProjStats()
        count = 5
        stat.count = count
        self.assertEqual(count, stat.count)

    def test_duration(self):
        stat = ProjStats()
        duration = timedelta(days =5, hours=10, minutes=3)
        stat.duration = duration
        self.assertEqual(duration, stat.duration)

    def test_tasks_list(self):
        stat = ProjStats()
        tasks = ["Task 1", "Task 2", "Task 3"]
        stat.tasks = tasks
        self.assertListEqual(tasks, stat.tasks)

    def test_append_to_tasks(self):
        stat = ProjStats()
        tasks = ["Task 1", "Task 2", "Task 3"]
        stat.tasks = tasks
        new_task = "New Task"
        stat.append_task(new_task)
        self.assertIn(new_task, stat.tasks)


    def test_delete_from_tasks(self):
        stat = ProjStats()
        tasks = ["Task 1", "Task 2", "Task 3"]
        stat.tasks = tasks
        removed_task = "Task 2"
        stat.remove_task(removed_task)
        self.assertNotIn(removed_task, stat.tasks)
