###############################################################
# simple queue implementation using []
# methods implemented :
#   enqueue (offer), dequeue(poll), peek, isFull, isEmpty
###############################################################


class QueueWithArray:
    def __init__(self, size):
        self.max_size = size
        self.size = 0
        self.data = []

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size

    def enqueue(self, val) -> bool:
        if self.isFull():
            print(f"queue is full")
            return False

        self.data.insert(0, val)
        self.size = self.size + 1
        return True

    def dequeue(self):
        if self.isEmpty():
            print(f"queue is empty")
            return -1

        val = self.data.pop()
        self.size = self.size - 1

        return val

    def peek(self):
        return self.data[self.size - 1]

    def print(self) -> None:
        if self.isEmpty():
            print(f"queue is empty")
            return

        out = ""
        i = self.size - 1

        while i > -1:
            out = out + " " + str(self.data[i])
            i = i - 1

        print(out)
        return
