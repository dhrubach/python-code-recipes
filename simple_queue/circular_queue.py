###############################################################
# LeetCode Problem Number : 622
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/design-circular-queue/
###############################################################
class CircularQueue:
    def __init__(self, size):
        """initialize your data structure here"""
        self.max_size = size

        """ set head and tail pointer to -1 """
        self.head = -1
        self.tail = -1

        """ initialize internal array """
        self.data = [[] for _ in range(size)]

    def isEmpty(self) -> bool:
        """checks whether the circular queue is empty or not"""
        return self.computeSize() == 0

    def isFull(self) -> bool:
        """checks whether the circular queue is full or not"""
        return self.computeSize() == self.max_size

    def enqueue(self, val: int) -> bool:
        """insert an element into the circular queue
        return true if the operation is successful
        """
        if self.isFull():
            return False

        """ move tail pointer to the next valid index
            example : max_size : 5, tail : 2, next tail : 3
                      max_size : 5, tail : 4, next tail : 0
        """
        self.tail = (self.tail + 1) % self.max_size
        self.data[self.tail] = val

        """ for the first enqueue operation, set head to point to tail """
        if self.head == -1:
            self.head = self.tail

        return True

    def dequeue(self) -> bool:
        """delete an element from the circular queue
        return true if the operation is successful
        """
        if self.isEmpty():
            return False

        self.data[self.head] = None

        """ if empty queue, set head to -1
            else move head to the next valid insert position
        """
        self.head = -1 if self.computeSize() == 1 else (self.head + 1) % self.max_size

        """ reset tail pointer for an empty queue """
        if self.head == -1:
            self.tail = -1

        return True

    def front(self) -> int:
        """get the front item from the queue"""
        if self.isEmpty():
            return -1

        """ return value pointed by head pointer """
        return self.data[self.head]

    def rear(self) -> int:
        """get the last item from the queue"""
        if self.isEmpty():
            return -1

        """ return value pointed by tail pointer """
        return self.data[self.tail]

    def computeSize(self) -> int:
        """ queue is empty if head pointer is set to -1 """
        if self.head == -1:
            return 0

        """ if both head and tail pointers are set to the same index,
            then queue has only 1 item
          """
        if self.tail == self.head:
            return 1

        """ if tail points to an index after head, then current size : (tail - head) + 1
            if tail points to an index before head, then current size : (tail - head) + 1 + max-size
        """
        diff = self.tail - self.head
        return diff + 1 if diff > 0 else diff + 1 + self.max_size

    def executeCommands(self, command: str, operands: list):
        """Automate execution of large number of operations to test implementation.

        Not part of main queue implementation.
        """
        if command == "enQueue":
            return self.enqueue(operands[0])
        elif command == "deQueue":
            return self.dequeue()
        elif command == "Rear":
            return self.rear()
        elif command == "Front":
            return self.front()
        elif command == "isFull":
            return self.isFull()
        elif command == "isEmpty":
            return self.isEmpty()

        return
