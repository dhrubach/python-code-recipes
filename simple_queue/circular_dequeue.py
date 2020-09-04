###############################################################
# LeetCode Problem Number : 641
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/design-circular-deque/
###############################################################


class CircularDeQueue:
    def __init__(self, max_size: int):
        self.max_size = max_size
        self.head = -1
        self.tail = -1
        self.size = 0
        self.data = [[] for _ in range(max_size)]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size

    def insertFront(self, val: int) -> bool:
        if self.isFull():
            return False

        if self.head == -1:
            self.head = 0
        else:
            self.head = self.max_size - 1 if self.head == 0 else self.head - 1
        self.data[self.head] = val
        self.size = self.size + 1

        if self.tail == -1:
            self.tail = self.head

        return True

    def insertLast(self, val: int) -> bool:
        if self.isFull():
            return False

        self.tail = (self.tail + 1) % self.max_size
        self.data[self.tail] = val
        self.size = self.size + 1

        if self.head == -1:
            self.head = self.tail

        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self.data[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size = self.size - 1

        if self.size == 0:
            self.head = self.tail = -1

        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        self.data[self.tail] = None
        self.size = self.size - 1
        if self.size == 0:
            self.head = self.tail = -1
        else:
            self.tail = self.max_size - 1 if self.tail == 0 else self.tail - 1

        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1

        return self.data[self.head]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1

        return self.data[self.tail]

    def executeCommands(self, command: str, operands: list):
        """Automate execution of large number of operations to test implementation.

        Not part of main queue implementation.
        """
        if command == "insertFront":
            return self.insertFront(operands[0])
        elif command == "insertLast":
            return self.insertLast(operands[0])
        elif command == "deleteFront":
            return self.deleteFront()
        elif command == "deleteLast":
            return self.deleteLast()
        elif command == "getFront":
            return self.getFront()
        elif command == "getRear":
            return self.getRear()
        elif command == "isFull":
            return self.isFull()
        elif command == "isEmpty":
            return self.isEmpty()

        return
