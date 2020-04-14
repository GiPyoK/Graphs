
def earliest_ancestor(ancestors, starting_node):
    vertices = {}
    # traverse through ancestors and add to vertices
    for (p, c) in ancestors:
        # create Key: child, value: parent relationship 
        if c in vertices:
            vertices[c].append(p)
        else:
            vertices[c] = [p]

    # if the input individual has no parents, return -1
    if starting_node not in vertices:
        return -1
    
    # at this point, the starting node has at least one parent
    # get parents from starting node
    parents = vertices[starting_node]
    most_ancestors = []
    for parent in parents:
        # get ancestors of each parents
        ancestor_lists = get_longest_path(parent, vertices)
        # get the ancestor list that has the most ancestors
        for ancestor_list in ancestor_lists:
            if len(ancestor_list) > len(most_ancestors):
                most_ancestors = ancestor_list
            # if the number of ancestors are the same,
            # get the one with lower numeric ID
            elif len(ancestor_list) == len(most_ancestors):
                if ancestor_list[-1] < most_ancestors[-1]:
                    most_ancestors = ancestor_list
    
    return most_ancestors[-1]
    
# helper function to get the longest path(s) of ancestors from starting vertex
def get_longest_path(starting_vertex, vertices):
    # Create a stack and push starting vertex
    stack = Stack()
    stack.push([starting_vertex])
    # Create a set of traversed vertices
    visited = set()
    # Create a return array of paths
    paths = []
    # while stack is not empty
    while stack.size() > 0:
        # pop the first vertex
        path = stack.pop()
        # add to paths array
        paths.append(path)
        # if not visited
        if path[-1] not in visited:
            # Mark as visited
            visited.add(path[-1])
            # Push all neighbors
            parents = get_parents(path[-1], vertices)
            if parents is not None:
                for parent in parents:
                    if parent not in visited:
                        new_path = path + [parent]
                        stack.push(new_path)

    return_path = []
    # Get the longests paths
    for path in paths:
        if len(path) >= len(return_path):
            return_path.append(path)
    return return_path

# helper functions to get parents
def get_parents(vertex_id, vertices):
    if vertex_id in vertices:
        return vertices[vertex_id]
    else:
        return None


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



# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
# earliest_ancestor(test_ancestors, 6)

# 1: [10], 
# 3: [1, 2], 
# 5: [4], 
# 6: [3, 5], 
# 7: [5], 
# 8: [4, 11], 
# 9: [8]