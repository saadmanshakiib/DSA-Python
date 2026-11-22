
class Queue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)

        return "Empty Queue"

    def front(self):
        if not self.isEmpty():
            return self.items[0]

        return "Empty Queue"

    def rear(self):
        if not self.isEmpty():
            return self.items[-1]

        return "Empty Queue"

    def display(self):
        print(self.items)


queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)

queue.display()

print("Dequeued:", queue.dequeue())
print("Front:", queue.front())
print("Rear:", queue.rear())

queue.display()
