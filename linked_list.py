class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
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

  def prepend(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    else:
      new_node.next = self.head
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
    current.next = new_node

  def remove(self, index):
    if index == 0:
      self.head = self.head.next
      return
    current = self.head
    for i in range(index - 1):
      current = current.next
    current.next = current.next.next

  def reverse(self):
    current = self.head
    prev = None
    while current:
      next = current.next
      current.next = prev
      prev = current
      current = next
    self.head = prev

#Driver code
if __name__ == '__main__': 
  llist = LinkedList()
  llist.append("A")
  llist.append("B")
  llist.printList()
  llist.prepend("C")
  llist.printList()
  llist.insert(2, "D")
  llist.printList()
  llist.append("E")
  llist.printList()
  llist.remove(2)
  llist.printList()
  llist.reverse()
  llist.printList()
  