class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

# How to plan the problem:
# initialize a graph
# we have a relationship parent_child = pairs

# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

"""
def earliest_ancestor(ancestors, starting_node):
   # initialize the graph
   g = Graph()
   # iterate through the ancestor list
   for p,c in ancestors:
       # add key in tuple at current index as vertex in graph
       g.add_vertex(p)
       # add key in tuple at current index as vertex in graph
       g.add_vertex(c)
       # connect the keys with the add_edge method
       g.add_edge(g.add_vertex(p),g.add_vertex(c))
   # Create an empty stack
   s = Stack()
   # Push a path the starting node
   s.push([starting_node])
   # Create a set to store visited vertices
   # visited = set()
   # Set the farthest_path length to 1
   farthest_path_len = 1
   # set the earliest_ancestor by default to -1
   earliest_ancestor = -1
   # While the stack is empty
   while s.size()>0:
       # Pop the first PATH
       path = s.pop()
       p = path[-1]
       # if the length of the path longer/equal to the farthest_path length and the vertex is less than the current value of earliest_ancestor
       # OR the length of the current path is more than the farthest_path length
       if (len(path) >= farthest_path_len and p < earliest_ancestor) or (len(path) > farthest_path_len):
           # set the earliest_ancestor equal to p
           earliest_ancestor = p
           # set the farthest_path length equal to the length of the current path
           farthest_path_len = len(path)
       # Then add A PATH TO its neighbors to the back of the stack
       for neighbor in g.vertices[p]: 
           # copy the contents of the current path to a new path list
           copy_path = list(path)
           # APPEND THE neighbor TO THE BACK
           copy_path.append(neighbor)
           s.push(copy_path)
           return earliest_ancestor
"""

def earliest_ancestor(ancestors, starting_node):
    # initialize Graph
    g = Graph()
    # iterate over the ancestor list
    for pair in ancestors:
        g.add_vertex(pair[0])
        g.add_vertex(pair[1])
        # add edges to connect parent and children
        g.add_edge(pair[1], pair[0])
    # Create an empty queue
    q = Queue()
    # Enqueue the path to the starting vertex id
    q.enqueue([starting_node])
    # Set the farthest_path length to 1
    farthest_path_length = 1
    # set the earliest_ancestor by default to -1
    earliest_ancestor = -1
    # while the queue is not empty...
    while q.size() > 0 :
        # remove the first path list from queue
        path = q.dequeue()
        # set vert equal to the id of the last vert in the path list
        v = path[-1]
        # if the length of the path longer/equal to the farthest_path_length and the vertex is less than the current value of earliest_ancestor
        # OR the length of the current path is more than the farthest_path_length
        if (len(path) >= farthest_path_length and v < earliest_ancestor) or (len(path) > farthest_path_length):
            # set the earliest_ancestor equal to vertex
            earliest_ancestor = v
            # set the farthest_path_length equal to the length of the current path  
            farthest_path_length = len(path) 
        # Then add A PATH TO its neighbors to the back of the stack 
        for neighbor in g.vertices[v]: 
            # copy the contents of the current path to a new path list
            copy_path = list(path)
            # APPEND THE neighbor TO THE BACK
            copy_path.append(neighbor)
            # Add o the queue
            q.enqueue(copy_path)
    # Return the earliest_ancestor
    return earliest_ancestor








       
    