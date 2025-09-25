class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, x):
        n = Node(x)
        if not self.rear:
            self.front = self.rear = n
        else:
            self.rear.next = n
            self.rear = n

    def dequeue(self):
        if not self.front:
            return None
        x = self.front.data
        self.front = self.front.next
        if not self.front: self.rear = None
        return x

    def show(self):
        t, s = self.front, []
        while t:
            s.append(t.data)
            t = t.next
        return s

queue = Queue()

while True:
    print("\n1. Send Message")
    print("2. Receive Message")
    print("3. View Messages")
    print("4. Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        msg = str(input("Enter message: ").strip())
        if msg: 
            queue.enqueue(msg)
            print("Message sent.")
        else:
            print("Error: Empty message!")
            
    elif ch == "2":
        if queue.front:
            print("Delivered:", queue.dequeue())
        else:
            print("Error: No messages!")
            
    elif ch == "3":
        print("Remaining queue:", queue.show())
        
    elif ch == "4":
        break
        
    else:
        print("Invalid choice!")
