"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue  
        q = Queue()
        # Enqueue the path to the starting vertex id
        q.enqueue(starting_vertex)
        # Create a set to store visited vertices
        visited = set()
        # While queue not empty....
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # if that vertex is not in visited..
            if v not in visited:
                # for debug
                print(v) 
                # Mark it as visited...
                visited.add(v)
                # Then add all of its neighbors to the back of the queue
                for next_v in self.get_neighbors(v):
                    q.enqueue(next_v)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack 
        s = Stack()
        # Push the starting vertex id
        s.push(starting_vertex)
        # Create a set to store visited vertices
        visited = set()
        # While stack not empty...
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            # if that vertex is not in visited...
            if v not in visited:
                # Mark it as visited..
                visited.add(v)
                # debug
                print(v)
                # Then add all of its neighbors to the back of the stack
                for next_v in self.get_neighbors(v):
                    s.push(next_v)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Check if visited has been initialized
        if visited is None:
            # If not, initialize a set to store visited
            visited = set() 
        # Print the node as visited
        print(starting_vertex)
        # Mark the node as visited
        visited.add(starting_vertex)
        # Call DFT recursive on each neighbor that has not been visited
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)
                    
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue 
        q = Queue()
        # Enqueue A PATH TO the starting vertex ID
        q.enqueue([starting_vertex])
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first path
            path = q.dequeue()
            # Grab the last vertex from the PATH
            last_vertex = path[-1]
            # If that vertex has not been visited...
            if last_vertex not in visited:
                # CHECK IF IT'S THE TARGET
                if last_vertex == destination_vertex:
                    # IF SO, RETURN PATH
                    return path
                # Mark it as visited...
                visited.add(last_vertex)
                # for debug
                print(last_vertex)
                # Then add A PATH TO its neighbors to the back of the queue
                for next_vert in self.get_neighbors(last_vertex):
                    # new
                    new_path = path.copy()
                    new_path.append(next_vert)
                    q.enqueue(new_path)
                    

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty Stack 
        s = Stack()
        # Push A PATH TO the starting vertex ID
        s.push([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first PATH
            path = s.pop()
            # Grab the last vertex from the PATH
            last_vertex = path[-1]
            # If that vertex has not been visited...
            if last_vertex not in visited:
                # CHECK IF IT'S THE TARGET
                if last_vertex == destination_vertex:
                    # IF SO, RETURN PATH
                    return path
                # Mark it as visited...
                visited.add(last_vertex)
                # Then add A PATH TO its neighbors to the back of the queue
                for next_vertex in self.get_neighbors(last_vertex):
                    # new
                    new_path = path.copy()
                    # COPY THE PATH
                    new_path.append(next_vertex)
                    # APPEND THE NEIGHBOR TO THE BACK
                    s.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited = None, path = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # If visited is None
        if visited is None:
            # Create a set to store visited nodes
            visited = set()
        # If path is None
        if path is None:
            # Create list to store the path
            path = []
        # Mark starting node as visited
        visited.add(starting_vertex)
        # Mark vertex to the path
        path = path + [starting_vertex]
        #  CHECK IF IT'S THE TARGET
        if starting_vertex == destination_vertex:
            # IF SO, RETURN PATH
            return path
        # Otherwise, perform DFS_recursive on each unvisited neighbor
        for neighbor in self.get_neighbors(starting_vertex):
            # if neighbor not visited
            if neighbor not in visited:
                # add a new path
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path)
                # Check new path if is not there
                if new_path is not None:
                    # return new path
                    return new_path
                    # else return None
        return None

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
