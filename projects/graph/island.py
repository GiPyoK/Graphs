# Scrap paper and notes for graphs week!
# Day Two
# Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:
# islands = [[0, 1, 0, 1, 0],
#            [1, 1, 0, 1, 1],
#            [0, 0, 1, 0, 0],
#            [1, 0, 1, 0, 0],
#            [1, 1, 0, 0, 0]]

# island_counter(islands) # returns 4
# Keywords
# islands - they consist of connected components
# connected - the neighbors (edges)
# directions - north, south, east, west (edges)
# 2d array - the grap
# returns the number of islands 

# How could we write a get neighbor function that uses this shape?
def get_neighbors(2d_arr, x, y):
    neighbors = []
    max_X, max_Y = len(2d_arr) - 1
    # Check North
    if y - 1 >= 0:
        if 2d_arr[y - 1][x] == 1:
            neighbors.append([x, y - 1])
    # Check South
    if y + 1 <= max_Y:
        if 2darr[y + 1][x] == 1:
            neighbors.append[x, y + 1]
    # Check East
    if x + 1 <= max_X:
        if 2darr[y][x + 1] == 1:
            neighbors.append[x + 1, y]
    # Check West
    if x - 1 >= 0:
        if 2darr[y][x - 1] == 1:
            neighbors.append[x - 1][y]
            
    if len(neighbors) > 0:
        return neighbors
    else:
        return None


# Offset coordinates, pick a 1 that checks north south east west
# How can we find the extent of an island?
# Either traversal method to find all nodes in island 
# How do I explore the larger set?
# Loop through and call a traversal if we find an unvisited 1

def get_islands(2d_arr):
    pass

