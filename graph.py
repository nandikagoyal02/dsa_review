# Edge List
graph = [[0,2], [2,3], [2,1], [1,3]]
# 0 connected to 2, 2 connected to 3 and 1, 1 connected to 3, etc

# Adjacency List
graph = [[2], [2,3], [1,3,4], [1]]
# Index is node and value is node's neighbors: 0 connected to 2, 1 connected to 2 and 3, 2 connected to 1, 3, 4, etc.

# Adjacency Matrix
# 0s and 1s, 0 means no connection, 1 means connection for whether node x has connection to node y: 0 is connected to 2, 1 is connected to 2 and 3, 2 is connected to 1, 3, 4, etc.
# Can use weights instead of 1s and 0s
graph = [
  [0,0,1,0], 
  [0,0,1,1],
  [1,1,0,1],
  [0,1,1,0]
]

# Adjacency List w Hash Table
class Graph:
  def __init__(self):
    self.number_of_nodes = 0
    self.adjacent_list = {}

  def add_vertex(self, node):
    self.adjacent_list[node] = []
    self.number_of_nodes += 1  

  def add_edge(self, node1, node2):
    # undirected graph
    self.adjacent_list[node1].append(node2)
    self.adjacent_list[node2].append(node1)

  def show_connections(self):
    for node in self.adjacent_list:
      connections = " ".join(self.adjacent_list[node])
      print(f"{node} --> {connections}")

my_graph = Graph()
my_graph.add_vertex("0")
my_graph.add_vertex("1")
my_graph.add_vertex("2")
my_graph.add_vertex("3")
my_graph.add_vertex("4")
my_graph.add_vertex("5")
my_graph.add_vertex("6")

my_graph.add_edge("3", "1")
my_graph.add_edge("3", "4")
my_graph.add_edge("4", "2")
my_graph.add_edge("4", "5")
my_graph.add_edge("1", "2")
my_graph.add_edge("1", "0")
my_graph.add_edge("0", "2")
my_graph.add_edge("6", "5")

my_graph.show_connections()