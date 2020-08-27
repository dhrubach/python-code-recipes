from list_node import ListNode
from remove_duplicates_all import RemoveAllDuplicates
from utility import printList

import unittest


class RemoveAllDuplicatesTest(unittest.TestCase):
    def setUp(self):
        self.linked_list = RemoveAllDuplicates()

    def test_single_node(self):
        l = ListNode(1)

        self.assertEqual(self.linked_list.deleteDuplicates(l), l)

    def test_double_nodes(self):
        tail = ListNode(1, None)
        head = ListNode(1, tail)

        self.assertIsNone(self.linked_list.deleteDuplicates(head))

    def test_remove_duplicates(self):
        tail = ListNode(3, None)
        l = ListNode(3, tail)
        l = ListNode(2, l)
        l = ListNode(1, l)
        head = ListNode(1, l)

        new_list = self.linked_list.deleteDuplicates(head)
        printList(new_list, "de-duplicated list")

        self.assertEqual(new_list.val, 2)
        self.assertIsNone(new_list.next)

    def test_remove_all_duplicates(self):
        tail = ListNode(3, None)
        l = ListNode(3, tail)
        l = ListNode(1, l)
        head = ListNode(1, l)

        self.assertIsNone(self.linked_list.deleteDuplicates(head))
