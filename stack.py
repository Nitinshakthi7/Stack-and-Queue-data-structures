class Stack:
    def __init__(self, capacity=5):
        self.stack = []
        self.capacity = capacity

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.capacity

    def push(self, item):
        if self.is_full():
            print("Stack Overflow!")
            return
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            print("Stack Underflow!")
            return None
        return self.stack.pop()

    def peek(self):
        return None if self.is_empty() else self.stack[-1]

def check_balanced(expr):
    s = Stack(len(expr))
    for ch in expr:
        if ch in "([": s.push(ch)
        elif ch in ")]":
            top = s.pop()
            if (ch==")" and top!="(") or (ch=="]" and top!="["): return False
    return s.is_empty()

expr = input("Enter: ")
print("Balanced" if check_balanced(expr) else "Not Balanced")