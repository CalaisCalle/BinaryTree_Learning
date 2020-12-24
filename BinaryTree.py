class Node():

    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, value):

        if (not self.value):
            #value becomes data
            self.value = value
        elif (not self.left):
            self.left = Node(value)
        elif (not self.right):
            self.right = Node(value)
        elif (self.right and self.left):
            self.left.left = Node()
            self.left.left.insert(value) #oh no
            

