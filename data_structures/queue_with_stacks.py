class QueueWithStacks:

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def enqueue(self, item):
        self.stack_1.append(item)

    def dequeue(self):
        if len(self.stack_1) == 0:
            raise Exception()

        while len(self.stack_1) > 0:
            self.stack_2.append(self.stack_1.pop())

        dequeued_item = self.stack_2.pop()

        while len(self.stack_2) > 0:
            self.stack_1.append(self.stack_2.pop())

        return dequeued_item
