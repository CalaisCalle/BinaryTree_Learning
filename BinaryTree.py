class Node():

    def __init__(self, value=None, left=None, right=None):
        # This is a comment to mark a change
        self.value = value
        self.left = left
        self.right = right

    def insert(self, value):
        # Compare the new value with the parent node
        if self.value:
            #if parent value exists
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value
            
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.value)
        if self.right:
            self.right.PrintTree()

    def DFS(self, search_term):
        '''
        DFS: Depth First Search
        For now: returns True if the term is in the tree
        '''
        #check if node value matches. If not: check left
        if (self.value == search_term):
            return True
        if (self.left):
            return self.left.DFS(search_term)
        print(self.value)
        if (self.right):
            return self.right.DFS(search_term)
        return False

    def BFS(self, search_term):
        '''
        BFS: Breadth First Search
        '''
        pass

    def recursive_search(self, search_term):
        if self.value == None or self.value == search_term:
            return self
        if search_term < self.value:
            return(self.left.recursive_search(search_term))
        if search_term > self.value:
            return(self.right.recursive_search(search_term))


