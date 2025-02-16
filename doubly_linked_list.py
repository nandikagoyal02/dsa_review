# Doubly Linked List

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class DoublyLinkedList:
  def __init__(self):
    self.head = None
    
  def append(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    current = self.head
    while current.next:
      current = current.next
    current.next = new_node
    new_node.prev = current

  def prepend(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    new_node.next = self.head
    self.head.prev = new_node
    self.head = new_node

  def printList(self):
    array = []
    current = self.head
    while current:
      array.append(current.data)
      current = current.next
    print(array)

  def insert(self, index, data):
    new_node = Node(data)
    if index == 0:
      self.prepend(data)
      return
    current = self.head
    for i in range(index - 1):
      current = current.next
    new_node.next = current.next
    current.next.prev = new_node
    current.next = new_node
    new_node.prev = current

  def remove(self, index):
    if index == 0:
      self.head = self.head.next
      return
    current = self.head
    for i in range(index - 1):
      current = current.next
    current.next = current.next.next
    current.next.prev = current

  def reverse(self):
    current = self.head
    prev = None
    while current:
      next = current.next
      current.next = prev
      prev = current
      current = next
    self.head = prev

if __name__ == '__main__':
  dll = DoublyLinkedList()
  dll.append("A")
  dll.append("B")
  dll.append("C")
  dll.printList()  # ['A', 'B', 'C']

  dll.prepend("D")
  dll.printList()  # ['D', 'A', 'B', 'C']

  dll.insert(2, "E")
  dll.printList()  # ['D', 'A', 'E', 'B', 'C']

  dll.remove(3)
  dll.printList()  # ['D', 'A', 'E', 'C']

  dll.reverse()
  dll.printList()  # ['C', 'E', 'A', 'D']
      