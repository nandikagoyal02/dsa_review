# Queue Implementation

class Node:
  def __init__(self, value):
      self.value = value
      self.next = None

class Queue:
  def __init__(self):
      self.first = None
      self.last = None
      self.length = 0

  def peek(self):
      return self.first  # Returns the first node

  def enqueue(self, value):
      new_node = Node(value)
      if self.length == 0:
          self.first = new_node
          self.last = new_node
      else:
          self.last.next = new_node
          self.last = new_node
      self.length += 1
      return self  # Returning self for method chaining

  def dequeue(self):
      if not self.first:
          return None  # Queue is empty
      if self.first == self.last:
          self.last = None
      self.first = self.first.next
      self.length -= 1
      return self  # Returning self for method chaining

  def is_empty(self):
      return self.length == 0

  def print_queue(self):
      current = self.first
      queue_values = []
      while current:
          queue_values.append(current.value)
          current = current.next
      print(queue_values)

# Driver Code
myQueue = Queue()
myQueue.enqueue("Joy")
myQueue.enqueue("Matt")
myQueue.enqueue("Pavel")
myQueue.enqueue("Samir")
myQueue.dequeue()
print(myQueue.peek().value)  # Should return "Matt"
myQueue.print_queue()  # ['Matt', 'Pavel', 'Samir']

# Expected order of processing (FIFO):
# Joy (dequeued first)
# Matt (next to be dequeued)
# Pavel
# Samir
