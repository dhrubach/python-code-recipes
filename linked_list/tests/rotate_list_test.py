from linked_list.rotate_list import RotateList
from linked_list.list_node import ListNode
from linked_list.utility import printList

import unittest


class RotateListTest(unittest.TestCase):
    def setUp(self):
        self.linked_list = RotateList()

    def test_single_node(self):
        l = ListNode()

        self.assertEqual(self.linked_list.rotate(l, 2), l)

    def test_double_node(self):
        tail = ListNode(2, None)
        head = ListNode(1, tail)

        self.assertEqual(self.linked_list.rotate(head, 4), head)

    def test_rotate_nodes(self):
        tail = ListNode(5, None)
        l = ListNode(4, tail)
        l = ListNode(3, l)
        l = ListNode(2, l)
        l = ListNode(1, l)

        rlist = self.linked_list.rotate(l, 2)
        self.assertEqual(rlist.val, 4)

        tail = ListNode(2, None)
        l = ListNode(1, tail)
        l = ListNode(0, l)

        rlist = self.linked_list.rotate(l, 4)
        self.assertEqual(rlist.val, 2)
