# Given a binary tree, get the average value at each level of the tree

def find_average_amount_on_binary_tree_levels(tree_root_node):
    children = []

    if tree_root_node.left is not None:
        children.append(tree_root_node.left)

    if tree_root_node.right is not None:
        children.append(tree_root_node.right)

    return _get_average_value_on_level_nodes(children, [tree_root_node.value])


def _get_average_value_on_level_nodes(level_nodes, result):
    if len(level_nodes) == 0:
        return result

    next_level = []
    current_level_sum = 0

    for node in level_nodes:
        if node.left is not None:
            next_level.append(node.left)

        if node.right is not None:
            next_level.append(node.right)

        current_level_sum += node.value

    result.append(current_level_sum // len(level_nodes))

    return _get_average_value_on_level_nodes(next_level, result)
