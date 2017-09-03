# Scrap Paper File to try different Things

# Test How to build a task variable
from task import Task
import datetime

parent1 = Task()
parent1.name = "Parent Task 1"

parent2 = Task()
parent2.name = "Parent Task 2"

child1 = Task()
child1.name = "Child Task 1"

child2 = Task()
child2.name = "Child Task 2"

child3 = Task()
child3.name = "Child Task 3"

t = Task()
t.name ="Main Task"
t.completed =0.5
start = datetime.datetime(year=2017, month=10, day=1, hour=10, minute=15)
end = datetime.datetime(year=2017, month=10, day=2, hour=11, minute=25)
duration = datetime.timedelta(days=1, hours=1, minutes=10)
print("Start Date : {}".format(start))
t.planned_start = start
t.planned_duration = duration


#t.prerequisites.append(parent1)
#t.prerequisites.append(parent2)

#t.dependants.append(child1)
#t.dependants.append(child2)
#t.dependants.append(child3)

t.report()
#print("Task Name: {} , that is {} completed".format(t.name,t.completed))