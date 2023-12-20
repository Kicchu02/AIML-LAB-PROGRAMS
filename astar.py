h = {
    'A': 10,
    'B': 8,
    'C': 5,
    'D': 7,
    'E': 3,
    'F': 6,
    'G': 5,
    'H': 3,
    'I': 1,
    'J': 0
}

Graph_nodes = {
    'A': [('B', 6), ('F', 3)],
    'B': [('C', 3), ('D', 2)],
    'C': [('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 8)],
    'E': [('I', 5), ('J', 5)],
    'F': [('G', 1), ('H', 7)],
    'G': [('I', 3)],
    'H': [('I', 2)],
    'I': [('E', 5), ('J', 3)]
}

start_node = 'A'
goal_node = 'J'

class Open:
    def __init__(self, node, g, h):
        self.node = node
        self.g = g
        self.h = h
        self.f = g + h

# initialise the open list and closed list arrays
open_list = []
closed_list = []

# insert the start node in open list
start = Open(start_node, 0, h[start_node])
open_list.append(start)

while len(open_list) > 0:
    # sort open list according to f value
    open_list.sort(key=lambda x:x.f)

    # put 1st node of open list to closed list
    node = open_list[0].node
    closed_list.append(node)

    # check if goal node is reached
    if node == goal_node:
        break
    
    # add the children of the node to open list and then delete the parent from the open list
    children = Graph_nodes[node]
    for child in children:
        open_list.append(Open(child[0], child[1] + open_list[0].g, h[child[0]]))
    del open_list[0]

# print the answer (closed list)
print(closed_list)