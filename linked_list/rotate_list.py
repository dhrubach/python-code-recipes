##################################################
# LeetCode Problem Number : 61
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/rotate-list/
##################################################
from linked_list.list_node import ListNode


class RotateList:
    def rotate(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head

        tail = head
        length = 1

        """ find the length of the list and it's tail
        """
        while tail.next:
            tail = tail.next
            length = length + 1

        """ link the tail to its head making it a circular list
            example input : 1 -> 2 -> 3 -> 4 -> 5 -> None
            post linking : 1 -> 2 -> 3 -> 4 -> 5 -> back to head
        """
        tail.next = head

        """ calculate the number of steps to reach the node which will
            be the new tail after rotation

            if k is a multiple of length, then the list will remain as is
        """
        k = k % length

        """ move the tail to the new tail node
            example :
                1 -> 2 -> 3 -> 4 -> 5 -> back to head
                length 5
                k = 2

                3 steps are required to reach 3
        """
        for _ in range(length - k):
            tail = tail.next

        """ set ListNode(4) to be the new head
            set ListNode(3) to be the new tail
        """
        head = tail.next
        tail.next = None

        return head
