class Node:
  def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None

class BinarySearchTree:
  def __init__(self):
      self.root = None

  def insert(self, value):
      if not self.root:
          self.root = Node(value)
      else:
          self._insert_recursive(self.root, value)

  def _insert_recursive(self, node, value):
      if value < node.value:
          if node.left is None:
              node.left = Node(value)
          else:
              self._insert_recursive(node.left, value)
      else:
          if node.right is None:
              node.right = Node(value)
          else:
              self._insert_recursive(node.right, value)

  def breadth_first_search(self):
      if not self.root:
          return []
      queue = [self.root]
      result = []
      while queue:
          current_node = queue.pop(0)
          result.append(current_node.value)
          if current_node.left:
              queue.append(current_node.left)
          if current_node.right:
              queue.append(current_node.right)
      return result

  def breadth_first_search_recursive(self, queue=None, result=None):
    if queue is None:
        queue = [self.root] if self.root else []
    if result is None:
        result = []
    if not queue:
        return result
    current_node = queue.pop(0)
    result.append(current_node.value)
    if current_node.left:
        queue.append(current_node.left)
    if current_node.right:
        queue.append(current_node.right)
    return self.breadth_first_search_recursive(queue, result)

  def depth_first_search_in_order(self, node, result=None):
    if result is None:
        result = []
    if node:
        self.depth_first_search_in_order(node.left, result)
        result.append(node.value)
        self.depth_first_search_in_order(node.right, result)
    return result

  def depth_first_search_pre_order(self, node, result=None):
    if result is None:
        result = []
    if node:
        result.append(node.value)
        self.depth_first_search_pre_order(node.left, result)
        self.depth_first_search_pre_order(node.right, result)
    return result

  def depth_first_search_post_order(self, node, result=None):
    if result is None:
        result = []
    if node:
        self.depth_first_search_post_order(node.left, result)
        self.depth_first_search_post_order(node.right, result)
        result.append(node.value)
    return result

bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(2)
bst.insert(7)
bst.insert(12)
bst.insert(17)

print("BFS:", bst.breadth_first_search())
print("Recursive BFS:", bst.breadth_first_search_recursive())
print("In-Order Traversal:", bst.depth_first_search_in_order(bst.root))
print("Pre-Order Traversal:", bst.depth_first_search_pre_order(bst.root))
print("Post-Order Traversal:", bst.depth_first_search_post_order(bst.root))