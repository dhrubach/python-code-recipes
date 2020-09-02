from linked_list.single_linked_list import SingleLinkedList

import unittest


class SingleLinkedListTest(unittest.TestCase):
    def setUp(self):
        self.linked_list = SingleLinkedList()

    def test_get(self):
        """empty linked list"""
        self.assertEqual(self.linked_list.get(0), -1)

        self.linked_list.addAtHead(1)
        self.linked_list.addAtHead(2)
        self.assertEqual(self.linked_list.get(1), 1)

        """invaid index"""
        self.assertEqual(self.linked_list.get(10), -1)

    def test_add_at_head(self):
        self.linked_list.addAtHead(10)

        head = self.linked_list.head
        self.assertEqual(head["data"], 10)

    def test_add_at_tail(self):
        self.linked_list.addAtTail(100)

        curr = self.linked_list.head
        while curr["next"] is not None:
            curr = curr["next"]
        self.assertEqual(self.linked_list.tail["data"], curr["data"])

    def test_add_at_index(self):
        self.linked_list.addAtIndex(1, 2)
        self.assertIsNone(self.linked_list.head)
        self.assertIsNone(self.linked_list.tail)

        self.linked_list.addAtHead(10)
        self.linked_list.addAtIndex(1, 20)
        self.assertEqual(self.linked_list.get(1), 20)
        self.assertEqual(self.linked_list.tail["data"], 20)

        self.linked_list.addAtIndex(5, 50)
        self.assertEqual(self.linked_list.tail["data"], 20)

        self.linked_list.addAtTail(40)
        self.linked_list.addAtIndex(1, 50)
        self.assertEqual(self.linked_list.get(2), 20)

    def test_delete_at_index(self):
        self.linked_list.addAtHead(1)
        self.linked_list.deleteAtIndex(0)

        self.assertIsNone(self.linked_list.head)
        self.assertIsNone(self.linked_list.tail)

        self.linked_list.addAtHead(2)
        self.linked_list.addAtHead(1)
        self.linked_list.addAtTail(3)
        self.linked_list.deleteAtIndex(1)

        self.assertEqual(self.linked_list.get(1), 3)

    def test_overwrite_head(self):
        self.linked_list.addAtIndex(0, 10)
        self.linked_list.addAtIndex(0, 20)
        self.linked_list.addAtIndex(1, 30)

        self.assertEqual(self.linked_list.get(0), 20)
