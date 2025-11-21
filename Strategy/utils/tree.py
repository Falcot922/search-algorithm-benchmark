class Tree:
    def __init__(self, node, left, right):
        self.node = node
        self.right = right
        self.left = left 
        self.parent = None

    def add_parent(self, parent):
        self.parent = parent
    

    