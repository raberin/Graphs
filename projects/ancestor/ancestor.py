# BFS - Path to anscestor where starting node is child
# Build graph


def earliest_ancestor(ancestors, starting_node):
    # Graph of ancestors
    my_graph = make_graph(ancestors)
    # Where potential ancestors are stored
    oldest_gen = []
    # Create a stack
    s = []
    s.append([starting_node])
    # Create a set of traversed vertices
    visited = set()
    # WHile stack is not empty:
    while len(s) > 0:
        # Pop the first vertex
        path = s.pop()
        child = path[-1]
        # if not visited
        if child not in visited:
            # Checks if child has no parents == ancestor AND is not the starting_node
            # If so... append to oldest_gen list
            if child not in my_graph and child != starting_node:
                oldest_gen.append([child, len(path)])
            # print(visited)
            # Mark as visited
            visited.add(child)
            # If child has parents, loop through and attach neighbors
            if child in my_graph:
                for parent in my_graph[child]:
                    # Make a copy of the path
                    new_path = list(path)
                    # Append next vertex to copied path
                    new_path.append(parent)
                    # Push to stack
                    s.append(new_path)
    # If oldest_gen is filled...
    print(oldest_gen)
    if oldest_gen:
        return determine_ancestor(oldest_gen)
    # If not...
    else:
        return -1


def make_graph(ancestors):
    my_graph = {}
    for pair in ancestors:
        parent = pair[0]
        child = pair[1]
        if child not in my_graph:
            my_graph[child] = set()
        my_graph[child].add(parent)
    return my_graph


def determine_ancestor(ls):
    highest_length_index = 0
    highest_length = 0
    # Loop through and save the oldest ancestor
    for i in range(len(ls)):
        if ls[i][1] > highest_length:
            highest_length = ls[i][1]
            highest_length_index = i
    # Incase of same length, determine the lower numeric ID
    for i in range(len(ls)):
        # If same length
        if ls[highest_length_index][1] == ls[i][1]:
            # Which ancestor is lower id
            if ls[highest_length_index][0] > ls[i][0]:
                highest_length_index = i
    return ls[highest_length_index][0]


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 8))
