class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = BSTNode(data)
            return

        now = self.root
        while True:
            if data < now.data:
                if now.left is None:
                    now.left = BSTNode(data)
                    return
                now = now.left
            else:
                if now.right is None:
                    now.right = BSTNode(data)
                    return
                now = now.right

    def preorder(self):
        def _pre(node):
            if node is None:
                return
            print(" -> " + str(node.data), end="")
            _pre(node.left)
            _pre(node.right)

        _pre(self.root)
        print(" ")
    
    def is_empty(self):
        return self.root is None
    
    def inorder(self):
        def _in(node):
            if node is None:
                return
            _in(node.left)
            print(" -> " + str(node.data) ,end="")
            _in(node.right)
        _in(self.root)
        print(" ")

    def postorder(self):
        def _post(node):
            if node is None:
                return
            
            _post(node.left)
            _post(node.right)
            print(" -> " + str(node.data), end="")
        _post(self.root)
        print(" ")
    def traverse(self):
        if self.is_empty():
            print("This is an empty binary search tree.")
            return
        
        print("Preorder:",end="")
        self.preorder()

        print("Inorder:" , end="")
        self.inorder()

        print("Postorder:" , end="")
        self.postorder()

    def find_min(self):
        if self.is_empty():
            return None
        
        now = self.root

        while now.left is not None:
            now = now.left
        return now.data
    
    def find_max(self):
        if self.is_empty():
            return None
        
        now = self.root

        while now.right is not None:
            now = now.right
        return now.data
    
    def delete(self,data):
        data = int(data)
        real = False
        now  = self.root
        
        while now is not None:
            if data == now.data:
                real = True
                break
            elif data < now.data:
                now = now.left
            else:
                now = now.right
        
        if not real:
            print("Delete Error, "+ str(data) +" is not found in Binary Search Tree.")
            return
        
        self.root = self._delete_node(self.root,data)
        
    
    def _delete_node(self,node,data):
        if node is None:
            return None
        
        if data < node.data:
            node.left = self._delete_node(node.left,data)
        elif data > node.data:
            node.right = self._delete_node(node.right,data)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            max_node = node.left
            while max_node is not None:
                max_node = max_node.right

            node.data = max_node.data

            node.left = self._delete_node(node.left,max_node.data)
        return node

def main():
    my_bst = BST()
    while 1:
        text = input()
        if text == "Done":
            break
        condition, data = text.split(": ")
        if condition == "I":
            my_bst.insert(int(data))
        elif condition == "D":
            my_bst.delete(int(data))
        else:
            print("Invalid Condition")
    my_bst.traverse()
main()
