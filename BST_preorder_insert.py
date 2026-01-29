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


def main():
    bst = BST()
    n = int(input())
    i = 0
    while i < n:
        bst.insert(int(input()))
        i += 1

    print("Preorder:", end="")
    bst.preorder()

main()