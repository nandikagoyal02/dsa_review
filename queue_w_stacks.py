class CrazyQueue:
  def __init__(self):
      self.first = []
      self.last = []

  def enqueue(self, value):
      # Move all elements from `first` to `last`
      while self.first:
          self.last.append(self.first.pop())

      self.last.append(value)  # Push the new value

      return self  # Return self for method chaining

  def dequeue(self):
      # Move all elements from `last` to `first`
      while self.last:
          self.first.append(self.last.pop())

      if self.first:
          self.first.pop()  # Remove the front element

      return self  # Return self for method chaining

  def peek(self):
      if self.first:
          return self.first[-1]  # Top element in `first` is the front
      if self.last:
          return self.last[0]  # Bottom element in `last` is the front
      return None  # Queue is empty

  def print_queue(self):
      print("First Stack:", self.first)
      print("Last Stack:", self.last)

# Driver Code
myQueue = CrazyQueue()
print(myQueue.peek())  # None (Queue is empty)
myQueue.enqueue("Joy")
myQueue.enqueue("Matt")
myQueue.enqueue("Pavel")
print(myQueue.peek())  # "Joy"
print("========")
myQueue.dequeue()
myQueue.dequeue()
myQueue.dequeue()
print("========")
print(myQueue.peek())  # None (Queue is empty)
myQueue.print_queue()  # Shows both stacks
