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
        # Check if they exist
        if v1 in self.vertices and v2 in self.vertices:
            # Add the edge
            self.vertices[v1].add(v2)
        else:
            print("ERROR ADDING EDGE: Vertex not found")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a queue and enqueue starting vertex
        qq = Queue()
        qq.enqueue([starting_vertex])
        # Create a set of traversed vertices
        visited = set()
        # While queue is not empty:
        while qq.size() > 0:
            # Dequeue/pop the first vertex
            path = qq.dequeue()
            # Grab last vertex from path
            vertex = path[-1]
            # if not visited
            if vertex not in visited:
                # Do the thing!!
                print('vertex', vertex)
                # Mark as visited
                visited.add(vertex)
                # enqueue all neighbors
                for next_vert in self.get_neighbors(vertex):
                    # Make a copy of path
                    new_path = list(path)
                    # Add next_vert into new_path
                    new_path.append(next_vert)
                    # enqueue to queue
                    qq.enqueue(new_path)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a stack and push starting vertex
        s = Stack()
        s.push([starting_vertex])
        # Create a set of traversed vertices
        visited = set()
        # While stack is not empty:
        while s.size() > 0:
            # Pop the first vertex
            path = s.pop()
            vertex = path[-1]
            # if not visited
            if vertex not in visited:
                # Do what you wanted to do
                print('vertex', vertex)
                # Mark as visited
                visited.add(vertex)
                # push neighbors of current vertex into top of stack
                for next_vert in self.get_neighbors(vertex):
                    # Make a copy of the path
                    new_path = list(path)
                    # Append next vertex to copied path
                    new_path.append(next_vert)
                    # Push to stack
                    s.push(new_path)

    def dft_recursive(self, vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Base Case
        if vertex not in visited:
            print('vertex', vertex)
            visited.add(vertex)

            neighbors = self.get_neighbors(vertex)
            for neighbor in neighbors:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a queue and enqueue starting vertex
        qq = Queue()
        qq.enqueue([starting_vertex])
        # Create a set of traversed vertices
        visited = set()
        # While queue is not empty:
        while qq.size() > 0:
            # Dequeue/pop the first vertex
            path = qq.dequeue()
            # Grab last vertex from path
            vertex = path[-1]
            # if not visited
            if vertex not in visited:
                # CHECK IF ITS THE TARGET DESTINATION
                if vertex == destination_vertex:
                    return path
                # Do the thing!!
                print('vertex', vertex)
                # Mark as visited
                visited.add(vertex)
                # enqueue all neighbors
                for next_vert in self.get_neighbors(vertex):
                    # Make a copy of path
                    new_path = list(path)
                    # Add next_vert into new_path
                    new_path.append(next_vert)
                    # enqueue to queue
                    qq.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create a stack and push starting vertex
        s = Stack()
        s.push([starting_vertex])
        # Create a set of traversed vertices
        visited = set()
        # While stack is not empty:
        while s.size() > 0:
            # Pop the first vertex
            path = s.pop()
            vertex = path[-1]
            # if not visited
            if vertex not in visited:
                # CHECK IF ITS TARGET DESTINATION
                if vertex == destination_vertex:
                    return path
                # Do what you wanted to do
                print('vertex', vertex)
                # Mark as visited
                visited.add(vertex)
                # push neighbors of current vertex into top of stack
                for next_vert in self.get_neighbors(vertex):
                    # Make a copy of the path
                    new_path = list(path)
                    # Append next vertex to copied path
                    new_path.append(next_vert)
                    # Push to stack
                    s.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # Base Case
        # Check if starting_vertex is visited
        if starting_vertex not in visited:
            if starting_vertex == destination_vertex:
                return path
            # If not...
            visited.add(starting_vertex)
            new_path = list(path)
            new_path.append(starting_vertex)
            # If starting_vertex is destination...

            # Mark it as visited
            # Call DFS on each neighbor
            neighbors = self.get_neighbors(starting_vertex)
            for neighbor in neighbors:
                new_path = list(path)
                self.dfs_recursive(neighbor, destination_vertex, visited, path)
                if new_path is not None:
                    return new_path


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
    print('---')
    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    print('---')
    graph.dft_recursive(1)
    print('---')

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
    print("dfs_recursive", graph.dfs_recursive(1, 6))
