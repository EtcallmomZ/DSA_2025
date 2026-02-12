class Datanode:
    def __init__(self,data=None):
        self.data = data
        self.next = None


class SinglyLinkedListed:
    def __init__(self):
        self.count = 0
        self.head = None

    def traverse(self):
        curr = self.head
        if not curr:
            print("This is an empty list.")
            return
        while curr:
            end_char = " -> " if curr.next else ""
            print(curr.data, end=end_char)
            curr = curr.next

    def insert_back(self,data):
        node = Datanode(data)
        if self.head is None:
            self.head = node
            self.count += 1
        
        else:
            now = self.head
            while now.next is not None:
                now = now.next
            now.next = node
        self.count += 1

    def insert_front(self,data):
        node = Datanode(data)
        node.next = self.head
        self.head = data
        self.count += 1

    def insert_index(self,index,data):
        now = self.head
        now_index = 1
        while now.next is not None:
            if now_index == index:
                now.data = data
                return
            now = now.next
            now_index += 1

   
        
def main():
    node = SinglyLinkedListed()
    for _ in range(int(input())):
        node.insert_back(input())
    node.insert_index(int(input()),input())
    node.traverse()

main()
