class GraphNode:
    def __init__(self, label):
        self.label = label
        self.visited = False
        self.adjacents = []
