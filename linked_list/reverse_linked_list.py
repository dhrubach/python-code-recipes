###############################################################
# LeetCode Problem Number : 206
# Difficulty Level : Easy
# URL : https://leetcode.com/problems/reverse-linked-list/
###############################################################

from linked_list.list_node import ListNode
from linked_list.utility import printList


class SingleLinkedList:
    def reverse(self, head: ListNode):
        if not head or not head.next:
            return head

        """ new head of reveresed list"""
        new_head = ListNode()
        """ pointer to current head """
        old_head = head

        while old_head.next is not None:
            """ new head is the node after the old head """
            new_head = old_head.next

            """ mvove old head pointer forward """
            old_head.next = old_head.next.next

            """ new head points to the current head """
            new_head.next = head

            """ set current head as the new head """
            head = new_head

        return head

    def reverse_v2(self, head: ListNode):
        if not head or not head.next:
            return head

        pre, cur = None, head

        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex

        return pre


if __name__ == "__main__":
    l1 = ListNode(5, None)
    l1 = ListNode(4, l1)
    l1 = ListNode(3, l1)
    l1 = ListNode(2, l1)
    l1 = ListNode(1, l1)

    printList(l1, "original linked list")

    sll = SingleLinkedList()
    reversed_list = sll.reverse(l1)
    printList(reversed_list, "\nreversed linked list")

    printList(sll.reverse_v2(reversed_list), "\nreversed linked list - version two")
