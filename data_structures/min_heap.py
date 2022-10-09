class Heap:
    def __init__(self):
        self.items = []

    def insert(self, item):
        self.items.append(item)

        self.heapify_up()

    def heapify_up(self):
        i = len(self.items) - 1

        while _has_parent(i):
            if self.items[_get_parent_index(i)] > self.items[i]:
                temp = self.items[i]
                self.items[i] = self.items[_get_parent_index(i)]
                self.items[_get_parent_index(i)] = temp
                i = _get_parent_index(i)
            else:
                break

    def extract_min(self):
        if len(self.items) == 0:
            return None

        min_value = self.items[0]

        self.items[0] = self.items[len(self.items) - 1]
        self.items.pop()

        self.heapify_down()

        return min_value

    def heapify_down(self):
        i = 0

        while self._has_left_child(i):
            smaller_index = _get_left_index(i)

            if self._has_right_child(i) and self.items[_get_right_index(i)] < self.items[_get_left_index(i)]:
                smaller_index = _get_right_index(i)

            if self.items[smaller_index] < self.items[i]:
                temp = self.items[i]
                self.items[i] = self.items[smaller_index]
                self.items[smaller_index] = temp

                i = smaller_index
            else:
                break

    def peek_min(self):
        if len(self.items) > 0:
            return self.items[0]

    def _has_left_child(self, i):
        left_child_index = _get_left_index(i)

        return left_child_index < len(self.items)

    def _has_right_child(self, i):
        right_child_index = _get_right_index(i)

        return right_child_index < len(self.items)

    def print(self):
        print(self.items)


def _get_parent_index(i):
    return (i - 1) // 2


def _has_parent(i):
    parent = _get_parent_index(i)

    return parent >= 0


def _get_left_index(i):
    return (2 * i) + 1


def _get_right_index(i):
    return (2 * i) + 2
