class BSTNode:
    def __init__(self, data: int=None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    def insert(self,data):
        if self.root == None:
            self.root = BSTNode(data)
            return
        
        now = self.root
        while True:
            if data < now.data:
                if data.left is None:
                    now.left = BSTNode(data)
                    return
                now = now.left
            else:
                if data.right is None:
                    now.rigt = BSTNode(data)
                now = now.right
    def preorder():
        if r