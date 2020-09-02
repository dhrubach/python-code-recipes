from linked_list.list_cycle_start import SingleLinkedList
from linked_list.list_node import ListNode
import unittest


class SingleLinkedListTest(unittest.TestCase):
    def setUp(self):
        self.linked_list = SingleLinkedList()

    def test_empty_list(self):
        head = None

        self.assertIsNone(self.linked_list.detectCycleStartNode(head))

    def test_single_node(self):
        head = ListNode(1, None)

        self.assertIsNone(self.linked_list.detectCycleStartNode(head))

    def test_double_nodes(self):
        tail = ListNode(2, None)
        head = ListNode(1, tail)
        tail.next = head

        self.assertEqual(self.linked_list.detectCycleStartNode(head), head)

    def test_detect_node(self):
        tail = ListNode(5, None)
        node4 = ListNode(4, tail)
        node3 = ListNode(3, node4)
        node2 = ListNode(2, node3)
        head = ListNode(1, node2)

        tail.next = node3

        self.assertEqual(self.linked_list.detectCycleStartNode(head), node3)
