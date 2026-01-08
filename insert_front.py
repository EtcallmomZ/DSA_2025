class DataNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.count = 0
        self.head = None

    def traverse(self):
        if self.head is None:
            print("This is an empty list.")
            return
        
        now = self.head
        msg = "" 
        while now is not None:
            if msg == "":
                msg = str(now.data)  
            else:
                msg = msg + " -> " + str(now.data) 
            now = now.next
        print(msg)

    def insert_last(self, data):
        node = DataNode(data)
        if self.head is None:
            self.head = node
        else:
            now = self.head
            while now.next is not None:
                now = now.next
            now.next = node
        self.count = self.count + 1

    def insert_front(self, data):
        node = DataNode(data)
        node.next = self.head
        self.head = node
        self.count = self.count + 1

    def insert_before(self, node_data, data):
        if self.head is None:
            print("Cannot insert, " + str(node_data) + " does not exist.")
            return
        
        if self.head.data == node_data:
            self.insert_front(data)
            return
        
        now = self.head
        while now.next is not None:
            if now.next.data == node_data:
                node = DataNode(data)
                node.next = now.next
                now.next = node
                self.count = self.count + 1
                return 
            now = now.next
        
        print("Cannot insert, " + str(node_data) + " does not exist.")

    def delete(self, data):
        if self.head is None:
            print("Cannot delete, " + str(data) + " does not exist.")
            return
        
        if self.head.data == data:
            self.head = self.head.next
            self.count = self.count - 1
            return
        
        now = self.head
        while now.next is not None:
            if now.next.data == data:
                now.next = now.next.next
                self.count = self.count - 1
                return
            now = now.next
            
        print("Cannot delete, " + str(data) + " does not exist.")

def main():
  mylist = SinglyLinkedList()
  for _ in range(int(input())):
    text = input()
    condition, data = text.split(": ")
    if condition == "F":
      mylist.insert_front(data)
    elif condition == "L":
      mylist.insert_last(data)
    # elif condition == "B":
    #     mylist.insert_before(*data.split(", "))
    # elif condition == "D":
    #     mylist.delete(data)
    else:
      print("Invalid Condition!")
  mylist.traverse()

main()