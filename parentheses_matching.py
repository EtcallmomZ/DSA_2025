""" parentheses matching """
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

def is_parentheses_matching(data):
    """ match or not """
    stack1 = ArrayStack()
    for i in data:
        stack1.push(i)
    stack2 = ArrayStack()
    stack3 = ArrayStack()
    stack4 = ArrayStack()
    for i in stack1.print_stack():
        if i == "(":
            stack2.push(i)
            stack3.push(i)
        else:
            if i == ")":
                if stack1.is_empty():
                    print(f"Parentheses in {data} are unmatched")
                    return False
                stack2.pop()
                stack4.push(i)
    if not stack2.is_empty() or stack3.get_size() != stack4.get_size():
        print(f"Parentheses in {data} are unmatched")
        return False
    print(f"Parentheses in {data} are matched")
    return True

print(is_parentheses_matching(input()))
