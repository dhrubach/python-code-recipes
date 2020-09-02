###############################################################
# LeetCode Problem Number : 203
# Difficulty Level : Easy
# URL : https://leetcode.com/problems/remove-linked-list-elements/
###############################################################

from linked_list.list_node import ListNode
from linked_list.utility import printList

class SingleLinkedList:
    def removeElements(self, head: ListNode, val: int):
        if not head:
            return

        curr = head

        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        if head.val == val:
            return head.next

        return head


if __name__ == "__main__":
    l = ListNode(5, None)
    l = ListNode(1, l)
    l = ListNode(3, l)
    l = ListNode(1, l)
    l = ListNode(1, l)
    l = ListNode(1, l)

    printList(l)

    print("\nlist after elements removed")
    linked_list = SingleLinkedList()
    printList(linked_list.removeElements(l, 1))

