# Scrap Paper File to try different Things

# Test How to build a task variable
from task import Task
import datetime

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

#t.prerequisites.append(parent1)
#t.prerequisites.append(parent2)

#t.dependants.append(child1)
#t.dependants.append(child2)
#t.dependants.append(child3)

root.report()
l1a.report()
print(c_up.__len__())
print("All Prerequisites" )
for parent in c_up:
    print(parent.id)
#print("Task Name: {} , that is {} completed".format(t.name,t.completed))