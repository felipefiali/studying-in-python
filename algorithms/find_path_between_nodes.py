from data_structures.graph_node import *


def find_path(tuple_list, start, finish):
    graph_hash_table = construct_graph_hash_table_from_tuple_list(tuple_list)

    bfs_list = []
    current_path = []

    start_node = graph_hash_table[start]
    bfs_list.append(start_node)

    while len(bfs_list) != 0:
        current_node = bfs_list.pop()

        current_path.append(current_node.label)

        current_node.visited = True

        if current_node.label == finish:
            return current_path

        for adjacent in current_node.adjacents:
            if not adjacent.visited:
                bfs_list.append(adjacent)

    print('no path found')
    return


def construct_graph_hash_table_from_tuple_list(tuple_list):
    node_hash_table = {}

    for start, end in tuple_list:
        if end not in node_hash_table:
            end_node = GraphNode(end)
            node_hash_table[end] = end_node

        end_node = node_hash_table[end]

        if start not in node_hash_table:
            start_node = GraphNode(start)
            node_hash_table[start] = start_node

        start_node = node_hash_table[start]

        if end_node not in start_node.adjacents:
            start_node.adjacents.append(end_node)

    return node_hash_table
