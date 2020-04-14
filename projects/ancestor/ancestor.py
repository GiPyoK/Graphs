
def earliest_ancestor(ancestors, starting_node):
    vertices = {}
    # traverse through ancestors and add to vertices
    for (p, c) in ancestors:
        # create Key: parent, value: child relationship
        if p in vertices:
            vertices[p]["c"].append(c)
        else:
            vertices[p] = {"p":[], "c":[c]}
        # create Key: child, value: parent relationship
        if c in vertices:
            vertices[c]["p"].append(p)
        else:
            vertices[c] = {"p": [p], "c":[]}

    



test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(test_ancestors, 1)