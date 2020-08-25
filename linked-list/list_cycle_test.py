from list_cycle import SingleLinkedList
from list_node import ListNode
import unittest


class SingleLinkedListTest(unittest.TestCase):
    def setUp(self):
        self.linked_list = SingleLinkedList()

    def test_empty_list(self):
        head = None

        self.assertFalse(self.linked_list.hasCycle(head))

    def test_single_node(self):
        head = ListNode(1, None)

        self.assertFalse(self.linked_list.hasCycle(head))

    def test_double_nodes(self):
        tail = ListNode(2, None)
        head = ListNode(1, tail)

        self.assertFalse(self.linked_list.hasCycle(head))

        tail.next = head

        self.assertTrue(self.linked_list.hasCycle(head))

    def test_has_cycle(self):
        tail = ListNode(5, None)
        node4 = ListNode(4, tail)
        node3 = ListNode(3, node4)
        node2 = ListNode(2, node3)
        head = ListNode(1, node2)

        self.assertFalse(self.linked_list.hasCycle(head))

        tail.next = node3

        self.assertTrue(self.linked_list.hasCycle(head))
