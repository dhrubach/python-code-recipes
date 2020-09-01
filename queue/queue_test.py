from queue.queue_array import QueueWithArray
from queue.queue_linked_list import QueueWithLinkedList

import unittest


class QueueWithArrayTest(unittest.TestCase):
    def setUp(self):
        self.queue_array = QueueWithArray(5)
        self.queue_list = QueueWithLinkedList(5)

    def test_array_enqueue(self):
        self.queue_array.enqueue(1)
        self.queue_array.enqueue(2)
        self.queue_array.enqueue(3)
        self.queue_array.enqueue(4)
        self.queue_array.enqueue(5)

        self.queue_array.print()

        self.assertEqual(self.queue_array.peek(), 1)

    def test_array_dequeue(self):
        val = self.queue_array.dequeue()
        self.assertEqual(val, -1)

        self.queue_array.enqueue(10)
        self.queue_array.enqueue(20)
        val = self.queue_array.dequeue()
        self.assertEqual(val, 10)

        self.queue_array.print()

    def test_array_queue_is_full(self):
        for i in range(5):
            self.queue_array.enqueue(i)

        self.assertFalse(self.queue_array.enqueue(6))

    def test_list_enqueue(self):
        self.queue_list.enqueue(1)
        self.queue_list.enqueue(2)
        self.queue_list.enqueue(3)
        self.queue_list.enqueue(4)
        self.queue_list.enqueue(5)

        self.queue_list.print()

        self.assertEqual(self.queue_list.peek(), 1)

    def test_list_dequeue(self):
        val = self.queue_list.dequeue()
        self.assertEqual(val, -1)

        self.queue_list.enqueue(10)
        self.queue_list.enqueue(20)
        val = self.queue_list.dequeue()
        self.assertEqual(val, 10)

        self.queue_array.print()

    def test_list_queue_is_full(self):
        for i in range(5):
            self.queue_array.enqueue(i)

        self.assertFalse(self.queue_array.enqueue(6))
