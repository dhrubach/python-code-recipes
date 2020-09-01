class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class QueueWithLinkedList:
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.head = None
        self.tail = None

    def isEmpty(self) -> bool:
        return not self.head

    def isFull(self) -> bool:
        return self.max_size == self.size

    def enqueue(self, val) -> bool:
        """ return false if queue is already full """
        if self.isFull():
            print(f"queue is full")
            return False

        """ create a new list node """
        node = ListNode(val)

        """ check if queue is empty 
            if true, then both head and tail will point to the same node
        """
        if self.isEmpty():
            self.head = self.tail = node
            self.size = self.size + 1
            return True

        """ for an existing queue, point current tail to the new node
            and move the tail pointer forward
            increase the size of the queue
        """
        self.tail.next = node
        self.tail = self.tail.next
        self.size = self.size + 1

        return True

    def dequeue(self) -> int:
        """ return -1 if queue is empty """
        if self.isEmpty():
            print(f"queue is empty")
            return -1

        """ return value from top of the list and move
            head pointer forward
        """
        rval = self.head.val
        self.head = self.head.next
        self.size = self.size - 1

        return rval

    def peek(self) -> int:
        if self.isEmpty():
            print(f"queue is empty")
            return -1

        """ return the value from the beginning of the list """
        return self.head.val

    def print(self) -> None:
        if self.isEmpty():
            print(f"queue is empty")
            return

        out = ""
        curr = head

        while curr:
            out = out + " " + str(curr.val)
            curr = curr.next

        print(out)
        return
