class CircularQueue:
    def __init__(self, size):
        self.max_size = size
        self.head = 0
        self.tail = 0
        self.data = []

    def isEmpty(self) -> bool:
        return len(self.data) == 0

    def isFull(self) -> bool:
        return len(self.data) == self.max_size

    def enqueue(self, val: int) -> bool:
        if self.isFull():
            return False

        self.data[self.tail] = val
        self.tail = (self.tail + 1) % self.max_size

        return True

    def dequeue(self) -> bool:
        if self.isEmpty():
            return False

        self.data[self.head] = None
        self.head = (self.head + 1) % self.max_size

        return True

