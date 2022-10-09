class Heap:
    def __init__(self):
        self.items = []

    def insert(self, item):
        self.items.append(item)

        self.min_heapify()

    def min_heapify(self):
        i = len(self.items) - 1

        while _has_parent(i):
            if self.items[_get_parent_index(i)] > self.items[i]:
                temp = self.items[i]
                self.items[i] = self.items[_get_parent_index(i)]
                self.items[_get_parent_index(i)] = temp
                i = _get_parent_index(i)
            else:
                break

    def remove_min(self):
        if len(self.items) == 0:
            return None

        min_value = self.items[0]

        self.items[0] = self.items[len(self.items) - 1]
        self.items.pop()

        self.min_heapify()

        return min_value

    def print(self):
        print(self.items)


def _get_parent_index(i):
    return (i - 1) // 2


def _has_parent(i):
    parent = _get_parent_index(i)

    return parent >= 0


