class Stack:
  def __init__(self):
      self.array = []

  def peek(self):
      return self.array[-1] if self.array else None  # Return last element, or None if empty

  def push(self, value):
      self.array.append(value)
      return self  # Returning self for method chaining

  def pop(self):
      if self.array:
          self.array.pop()
      return self  # Returning self for method chaining

# Driver Code
myStack = Stack()
print(myStack.peek())  # None (Stack is empty)

myStack.push('google')
myStack.push('ztm')
myStack.push('discord')
print(myStack.peek())  # discord

myStack.pop()
myStack.pop()
myStack.pop()

# Expected order of removal:
# discord
# ztm
# google
