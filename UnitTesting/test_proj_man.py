from unittest import TestCase
from PyProjManCore.proj_man import ProjMan
from PyProjManCore.task import Task


class TestProjMan(TestCase):
    def test_init(self):
        """Check Type of ProjMan"""
        pm = ProjMan()
        self.assertIsInstance(pm, ProjMan)

    def test_root(self):
        """Can create a new project with a root Task"""
        root = Task("Root Task")
        pm = ProjMan(root)
        self.assertEqual(root, pm.root)

    def test_name(self):
        """Can we define a name in the constructor?"""
        project_name = "Some Project Name"
        pm = ProjMan(None,project_name)
        self.assertEqual(project_name, pm.name)

    def test_add_child(self):
        """PM Can add a child"""
        root = Task("Root Task")
        pm = ProjMan(root)
        child = Task("Child Task")
        pm.add_child(child)
        self.assertIn(child, root.dependants)

    def test_add_child2(self):
        """PM Adding a child implies root is a parent for the child"""
        root = Task("Root Task")
        pm = ProjMan(root)
        child = Task("Child Task")
        pm.add_child(child)
        self.assertIn(root, child.prerequisites)

    def test_add_parent(self):
        """Can Add Parent to Root Task"""
        root = Task("Root Task")
        pm = ProjMan(root)
        parent = Task("Parent Task")
        pm.add_parent(parent)
        self.assertIn(parent, root.prerequisites)

    def test_add_parent_rebase1(self):
        """Adding Parent to root Task, Rebase Root to Parent"""
        root = Task("Root Task")
        pm = ProjMan(root)
        parent = Task("Parent Task")
        pm.add_parent(parent)
        self.assertEqual(parent, pm.root)

    def test_add_parent_rebase2(self):
        """Adding Parent to root Task, Makes former root a child to parent"""
        root = Task("Root Task")
        pm = ProjMan(root)
        parent = Task("Parent Task")
        pm.add_parent(parent)
        self.assertIn(root, pm.root.dependants)

    def test_list_tasks(self):
        """Listing all tasks in a project"""
        # Create Root
        root = Task("Root Task")
        # Create Project 
        pm = ProjMan(root)
        # Append Children 
        child1 = Task("Child Task 1")
        pm.add_child(child1)

        child2 = Task("Child Task 2")
        pm.add_child(child2)

        task_list = pm.list_tasks()
        self.assertTrue(
            root in task_list and 
            child1 in task_list and 
            child2 in task_list)

    def test_list_tasks_duplicates(self):
        """Listing all tasks in a project, no duplicates"""
        # Create Root
        root = Task("Root Task")
        # Create Project
        pm = ProjMan(root)
        # Append Children
        child1 = Task("Child Task 1")
        pm.add_child(child1)

        child2 = Task("Child Task 2")
        pm.add_child(child2)

        task_list = pm.list_tasks()
        self.assertEqual(3,len(task_list))