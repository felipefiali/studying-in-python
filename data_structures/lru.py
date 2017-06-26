class LRUCache:
    def __init__(self, capacity):
        self.items = {}
        self.priority_queue = []
        self.capacity = capacity

    def put(self, key, value):
        if len(self.items) == self.capacity:
            self._remove_smallest_priority()

        self.items[key] = value

        self._update_priority_queue(key)

    def get(self, key):
        self._update_priority_queue(key)

        return self.items[key]

    def _update_priority_queue(self, key):
        if key in self.priority_queue:
            self.priority_queue.remove(key)

        self.priority_queue.append(key)

    def _remove_smallest_priority(self):
        item = self.priority_queue.pop(0)

        del self.items[item]
