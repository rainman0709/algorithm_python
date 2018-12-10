from Tree import *

elems = range(10)
tree = Create_Tree()
for i in elems:
    tree.add(i)

tree.travelsal_tree(tree.root)