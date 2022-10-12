"""
Given a binary search tree and two integers low and high,
return the sum of values in all nodes with a value in the range
"""


def sum_items_in_range_in_bst(tree_root, min, max):
    if tree_root is None:
        return 0

    if max >= tree_root.value >= min:
        return sum_items_in_range_in_bst(tree_root.left, min, max) + \
               sum_items_in_range_in_bst(tree_root.right, min, max) + \
               tree_root.value
    elif tree_root.value < min:
        return sum_items_in_range_in_bst(tree_root.right, min, max)
    elif tree_root.value > max:
        return sum_items_in_range_in_bst(tree_root.left, min, max)
