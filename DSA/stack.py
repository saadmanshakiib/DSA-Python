class Stack:
    def __init__(self):
        self.stack = []

    def push(self,element):
        self.stack.append(element)

    def pop(self):
        self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def print(self):
            print(f"{self.stack}")

print (f"Welcome to Stack")
myStack = Stack()

myStack.push(33)
myStack.push(22)
myStack.push(31)
myStack.push(12)
myStack.push(54)
print(f"Stack : ${myStack.print()}")

myStack.pop()
print(f"After Pop : ${myStack.print()}")

print(f"After Peek : ${myStack.peek()}")
print(f"Stack is Empty ? ${myStack.isEmpty()}")
print(f"Stack Size : ${myStack.size()}")


