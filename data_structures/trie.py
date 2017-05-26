class Node:
    def __init__(self):
        self.edges = {}
        self.prefix = None
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        if len(word) == 0:
            return

        current = self.root

        for index, character in enumerate(word):
            if character in current.edges:
                current = current.edges[character]
            else:
                new_node = Node()
                new_node.prefix = word[:index + 1]
                current.edges[character] = new_node
                current = new_node

        current.is_word = True

    def lookup(self, prefix):
        current = self.root

        suggestions = []

        for character in prefix:
            if character in current.edges:
                current = current.edges[character]

                if current.is_word:
                    suggestions.append(current.prefix)

        temp_edges = []
        temp_edges += list(current.edges.values())

        while len(temp_edges) > 0:
            current = temp_edges.pop()

            if current.is_word:
                suggestions.append(current.prefix)

            temp_edges += list(current.edges.values())

        return suggestions




