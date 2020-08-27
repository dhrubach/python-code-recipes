from list_node import ListNode
from remove_duplicates import RemoveDuplicates
from utility import printList

import unittest


class RemoveDuplicatesTest(unittest.TestCase):
    def setUp(self):
        self.linked_list = RemoveDuplicates()

    def test_single_node(self):
        l = ListNode(1)

        self.assertEqual(self.linked_list.deleteDuplicates(l), l)

    def test_double_nodes(self):
        tail = ListNode(1, None)
        head = ListNode(1, tail)

        new_list = self.linked_list.deleteDuplicates(head)
        self.assertEqual(new_list.val, head.val)

    def test_remove_duplicates(self):
        tail = ListNode(3, None)
        l = ListNode(3, tail)
        l = ListNode(2, l)
        l = ListNode(1, l)
        head = ListNode(1, l)

        new_list = self.linked_list.deleteDuplicates(head)
        printList(new_list, "de-duplicated list")

        self.assertEqual(new_list.next.val, 2)
