class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack is Empty"
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is Empty"
        return self.items[-1]

    def display(self):
        print(self.items)

    def is_empty(self):
        return len(self.items) == 0


stack = Stack()
stack.push(23)
stack.push(54)
stack.push(67)
stack.push(86)
stack.push(93)

stack.display()
stack.pop()
stack.display()
print(stack.peek())