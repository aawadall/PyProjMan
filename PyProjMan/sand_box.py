# Scrap Paper File to try different Things

# Test How to build a task variable
from PyProjMan.task import Task

t = Task()
print(t.id)
t.name ="Task 1"
t.completed =0.5
print("Task Name: {} , that is {} completed".format(t.name,t.completed))