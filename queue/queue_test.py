from queue_array import QueueWithArray

import unittest


class QueueWithArrayTest(unittest.TestCase):
    def setUp(self):
        self.queue_array = QueueWithArray(5)

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