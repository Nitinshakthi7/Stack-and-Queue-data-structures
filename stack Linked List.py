class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Linked_list:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:   
            return None
        popped = self.top.data
        self.top = self.top.next
        return popped
    
    def is_empty(self):
        return self.top is None
    
def is_balanced(expression):
    stack = Linked_list()
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in expression:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            if stack.is_empty() or stack.pop() != pairs[char]:
                return "Not Balanced"
            
    return "Balanced" if stack.is_empty() else "Not Balanced"
 

expression = input("Enter an expression: ")
print(is_balanced(expression))
