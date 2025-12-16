""" students groups """
class ArrayStack:
    """ here is how to crete """
    def __init__(self):
        """ create stack """
        self.size = 0
        self.data = []

    def push(self,input_data):
        """ push """
        input_data = str(input_data)
        if input_data.isdigit():
            input_data = int(input_data)
        elif input_data.replace(".","",1).isdigit():
            input_data = float(input_data)

        self.data.append(input_data)
        self.size += 1
    def pop(self):
        """ pop """
        if self.size > 0:
            self.size -= 1
            return self.data.pop(-1)
        return print("Underflow: Cannot pop data from an empty list")
    def is_empty(self):
        """ empty or not """
        if self.size <= 0:
            return True
        return False
    def get_stack_top(self):
        """ get stack top """
        if self.size > 0:
            return self.data[-1]
        return print("Underflow: Cannot get stack top from an empty list")
    def get_size(self):
        """ get_size """
        return self.size
    def print_stack(self):
        """ print_stack """
        return self.data
    def print_stack_v2(self):
        """ print stack v2 """
        for i in range(self.size):
            print(self.data[i], end='')
            if i < self.size -1:
                print(', ' , end='')
        print()


def student(n):
    """ i wanna die """
    l1 = []
    for _ in range(n):
        l1.append(ArrayStack())

    stack1 = ArrayStack()
    for _ in range(int(input())):
        stack1.push(input())

    current = 0

    while not stack1.is_empty():
        i = stack1.pop()

        l1[current].push(i)

        current = int((current + 1)%n)

    for j in range(n):
        print(f"Group {j+1}: " , end = "")
        l1[j].print_stack_v2()
student(int(input()))
