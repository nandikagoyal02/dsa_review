# Hash Table using Separate Chaining

# The ‘Node‘ class will represent a node in a linked list. 
# Each node will contain a key-value pair, as well as a pointer to the next node in the list.

# self ensures each instance maintains its own state.
# It allows methods to access and modify instance variables.
# Without self, Python assumes variables are local to the method, causing errors.

class Node: 
  def __init__(self, key, value): 
      self.key = key 
      self.value = value 
      self.next = None

# The ‘HashTable’ class will contain the array that will hold the linked lists, as well as methods to insert, retrieve, and delete data from the hash table.

class HashTable:
  def __init__(self, capacity):
    self.capacity = capacity # capacity (Total Storage)
    # The fixed number of slots (buckets) available in the hash table.
    self.size = 0 # size (Current Usage)
    # The actual number of key-value pairs stored in the table.
    self.table = [None] * capacity

  def _hash(self, key):
    return hash(key) % self.capacity
    # % self.capacity (modulus operator) restricts the hash value to a valid index range (0 to capacity - 1).

  def insert(self, key, value):
    index = self._hash(key) # This tells us where in the hash table we should store the given (key, value) pair.
    if self.table[index] is None:
      # If the bucket (slot) is empty, we create a new Node(key, value) and place it at self.table[index].
      self.table[index] = Node(key, value)
      self.size += 1
    else:
      # If the bucket is already occupied, we traverse the linked list stored at self.table[index].
      current = self.table[index]
      while current:
        # If the key already exists in the linked list, update its value.
        # This ensures that the same key doesn't get duplicated.
        if current.key == key:
          current.value = value
          return
        current = current.next
      # If the key wasn’t found, create a new Node(key, value).
      # Insert it at the head of the linked list stored in self.table[index].
      # (chaining method)
      new_node = Node(key, value)
      new_node.next = self.table[index]
      self.table[index] = new_node
      self.size += 1
      
  def search(self, key):
    index = self._hash(key)
    current = self.table[index]
    while current:
      if current.key == key:
        return current.value
      current = current.next
    raise KeyError(key)

  def remove(self, key): 
    index = self._hash(key) 
    previous = None
    current = self.table[index] 
    while current: 
        if current.key == key: 
            if previous: 
                previous.next = current.next
            else: 
                self.table[index] = current.next
            self.size -= 1
            return
        previous = current 
        current = current.next
    raise KeyError(key) 

  def __str__(self):
    elements = []
    for i in range (self.capacity):
      current = self.table[i]
      while current:
        elements.append((current.key, current.value))
        current = current.next
    return str(elements)

  def __len__(self): 
    return self.size 
  
  def __contains__(self, key): 
    try: 
        self.search(key) 
        return True
    except KeyError: 
        return False

# Driver code 
if __name__ == '__main__': 
    ht = HashTable(5) 

    ht.insert("apple", 3) 
    ht.insert("banana", 2) 
    ht.insert("cherry", 5) 

    print("apple" in ht)  # True 
    print("durian" in ht)  # False 

    print(ht.search("banana"))  # 2 

    ht.insert("banana", 4) 
    print(ht.search("banana"))  # 4 

    ht.remove("apple") 
    print(len(ht))  # 3 
  
    
    
    