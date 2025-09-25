class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self, capacity=5):
        self.queue = [None] * capacity
        self.capacity = capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):
        if self.is_full():
            print("Queue Overflow!")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow!")
            return None
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

queue = []

while True:
    print("\n1. Send Message")
    print("2. Receive Message")
    print("3. View Messages")
    print("4. Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        msg = input("Enter message: ").strip()
        if msg: 
            queue.append(msg)
            print("Message sent.")
        else:
            print("Error: Empty message!")
    elif ch == "2":
        if queue:
            print("Delivered:", queue.pop(0))
        else:
            print("Error: No messages!")
    elif ch == "3":
        print("Remaining queue:", queue)
    elif ch == "4":
        break
    else:
        print("Invalid choice!")
