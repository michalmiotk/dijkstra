from node import Node
from copy import copy

connections = {'1_3':18, '1_4':12, '1_5':30, '4_5':8, '5_6':10, '4_6':20, '3_5':15, '2_6':10, '3_2':27}
start_node = 1
goal_node = 6

def get_cost_from_to(node1, node2):
    for conn in connections.keys():
        some_node1, some_node2 = [int(c) for c in conn.split('_')]
        if node1 in [some_node1, some_node2] and node2 in [some_node1, some_node2]:
            return connections[conn]
    return None
def get_all_neighbours(node_nr):
    nodes = set()
    for key in connections.keys():
        node1, node2 = [int(node_nr) for node_nr in key.split('_')]
        if node_nr in [node1, node2]:
            for node in [node1,  node2]:
                nodes.add(node)
    return nodes

nodes_names = []
for key in connections.keys():
    node1, node2 = [int(node_nr) for node_nr in key.split('_')]
    for node in [node1,  node2]:
        if node not in nodes_names:
            nodes_names.append(node)

open_nodes = {}
closed = {}
for node_nr in nodes_names:
    if node_nr == start_node:
        open_nodes[node_nr] = Node(20, 20, 0)
    elif node_nr == goal_node:
        open_nodes[node_nr] = Node(0)
    else:
        open_nodes[node_nr] = Node(10)
    
node_to_delete = start_node

while open_nodes:
    deleted_node = open_nodes.pop(node_to_delete)
    closed[node_to_delete] = deleted_node
    if node_to_delete == goal_node:
        break
    for node_nr in open_nodes.keys():
        if node_nr not in get_all_neighbours(node_to_delete):
            continue
        tent_past_cost = deleted_node.past_cost + get_cost_from_to(node_nr, node_to_delete)
        if tent_past_cost < open_nodes[node_nr].past_cost:
            open_nodes[node_nr].past_cost = tent_past_cost
            open_nodes[node_nr].parent_node = node_to_delete

    if len(open_nodes) >1:
        for node, node_obj in sorted(open_nodes.items(), key=lambda e:e[1].optimistic_cost):
            if node != goal_node:
                node_to_delete = node
                break
            
    else:
        node_to_delete = goal_node

for key,val in closed.items():
    print(key, val)