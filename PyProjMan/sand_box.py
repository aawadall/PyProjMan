# Scrap Paper File to try different Things

# Test How to build a task variable
from PyProjMan.task import Task

root = Task("Root Task")

# Define 3 Layers of tasks
# Layer 1
l1a = Task("Prerequisite a, Layer 1")
l1b = Task("Prerequisite b, Layer 1")
root.append_prerequisite(l1a)
root.append_prerequisite(l1a)
root.append_prerequisite(l1b)
# Layer 2
l2a = Task("Prerequisite a, Layer 2")
l2b = Task("Prerequisite b, Layer 2")
l1a.append_prerequisite(l2a)
l1a.append_prerequisite(l2b)
l2c = Task("Prerequisite c, Layer 2")
l2d = Task("Prerequisite d, Layer 2")
l1b.append_prerequisite(l2c)
l1b.append_prerequisite(l2d)
# Layer 3
l3a = Task("Prerequisite a, Layer 3")
l2a.append_prerequisite(l3a)
l2b.append_prerequisite(l3a)
l3b = Task("Prerequisite b, Layer 3")
l2a.append_prerequisite(l3b)
# Assign each layer the layer over it as a prerequisite

c_up = root.crawl_up()

root.report()
l1a.report()
print(c_up.__len__())
print("All Prerequisites")
for parent in c_up:
    print(parent.id)
