class Node:
  def __init__(self, value):
      self.value = value
      self.next = None

class Stack:
  def __init__(self):
      self.top = None
      self.bottom = None
      self.length = 0

  def peek(self):
      return self.top  # Returns the top node

  def push(self, value):
      new_node = Node(value)
      if self.length == 0:
          self.top = new_node
          self.bottom = new_node
      else:
          holding_pointer = self.top
          self.top = new_node
          self.top.next = holding_pointer
      self.length += 1
      return self  # Returning self for method chaining

  def pop(self):
      if not self.top:
          return None  # Stack is empty
      if self.top == self.bottom:
          self.bottom = None
      self.top = self.top.next
      self.length -= 1
      return self  # Returning self for method chaining

  def is_empty(self):
      return self.length == 0

  def print_stack(self):
      current = self.top
      stack_values = []
      while current:
          stack_values.append(current.value)
          current = current.next
      print(stack_values)

# Driver Code
myStack = Stack()
print(myStack.push("google"))  # Push 'google'
print(myStack.push("google2"))  # Push 'google2'
print(myStack.peek().value)  # Should return "google2"
print(myStack.pop())  # Pop "google2"
print(myStack.pop())  # Pop "google"

# Expected output order (LIFO):
# google2 (top)
# google (bottom)
