from BinaryTree import Node
import numpy as np

xs = [i for i in range(100)]

root = Node()

for x in xs:
    root.insert(x)

root.PrintTree()

if(root.DFS(5)):
    print("Found 5")

if(root.recursive_search(5)):
    print("Found 5 (recursively)")
