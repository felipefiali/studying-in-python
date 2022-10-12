class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def with_left(self, tree_node):
        self.left = tree_node

        return self

    def with_right(self, tree_node):
        self.right = tree_node

        return self


class Tree:
    def __init__(self, root):
        self.root = root
