from BinaryTree import Node
import numpy as np

xs = [i for i in range(11)]

root = Node()

for x in xs:
    root.insert(x)

if(root.DFS(5)):
    print("Found 5")

if(not root.DFS(11)):
    print("Couldn't find 11")