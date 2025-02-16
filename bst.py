# Binary Search Tree 
class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, value):
    if self.root is None:
      self.root = Node(value)
    else:
      currentNode = self.root
      while True:
        if value < currentNode.value:
          if currentNode.left is None:
            currentNode.left = Node(value)
            return
          else:
            currentNode = currentNode.left
        else:
          if currentNode.right is None:
            currentNode.right = Node(value)
            return
          else:
            currentNode = currentNode.right
  
  def lookup(self, value):
    if self.root is None:
      return False
    else:
      currentNode = self.root
      while currentNode is not None:
        if value < currentNode.value:
          currentNode = currentNode.left
        elif value > currentNode.value:
          currentNode = currentNode.right
        else:
          return currentNode
      return None

  def remove(self, value):
    if self.root is None:
      return False
    else:
      currentNode = self.root
      parentNode = None
      while currentNode is not None:
        if value < currentNode.value:
          parentNode = currentNode
          currentNode = currentNode.left
        elif value > currentNode.value:
          parentNode = currentNode
          currentNode = currentNode.right 
        elif value == currentNode.value:
          # Option 1: No right child
          if currentNode.right is None:
            if parentNode is None:
              self.root = currentNode.left
            else:
              if currentNode.value < parentNode.value:
                parentNode.left = currentNode.left
              elif currentNode.value > parentNode.value:
                parentNode.right = currentNode.left
          # Option 2: Right child which doesnt have a left child
          elif currentNode.right.left is None:
            if parentNode is None:
              self.root = currentNode.left
            else:
              currentNode.right.left = currentNode.left
              if currentNode.value < parentNode.value:
                parentNode.left = currentNode.right
              elif currentNode.value > parentNode.value:
                parentNode.right = currentNode.right
          # Option 3: Right child that has a left child
          else:
            # Find the right child's left most child
            leftmost = currentNode.right.left
            leftmostParent = currentNode.right
            while leftmost.left is not None:
              leftmostParent = leftmost
              leftmost = leftmost.left
            currentNode.value = leftmost.value
            # Parent's left subtree is now leftmost's right subtree
            if leftmost.right is not None:
              leftmostParent.left = leftmost.right
            else:
              leftmostParent.left = None
          return True
      return False

  def inorder_traversal(self, node):
    if node is not None:
        self.inorder_traversal(node.left)
        print(node.value, end=" ")  # Print the node value
        self.inorder_traversal(node.right)

  def print_tree(self):
    self.inorder_traversal(self.root)
    print()  # Newline for clean output


# Test BST functions
bst = BinarySearchTree()
bst.insert(9)
bst.insert(4)
bst.insert(6)
bst.insert(20)
bst.insert(170)
bst.insert(15)
bst.insert(1)
bst.print_tree()
print(bst.lookup(9))
print(bst.lookup(4))
print(bst.lookup(6))
print(bst.lookup(20))
print(bst.lookup(170))
print(bst.lookup(15))
print(bst.lookup(1))
print(bst.lookup(0))
print(bst.lookup(2))
print(bst.remove(9))
bst.print_tree()