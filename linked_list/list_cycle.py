###############################################################
# LeetCode Problem Number : 141
# Difficulty Level : Easy
# URL : https://leetcode.com/problems/linked-list-cycle/
###############################################################

from linked_list.list_node import ListNode


class SingleLinkedList:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        fp = sp = head

        while fp and fp.next:
            fp = fp.next.next
            sp = sp.next
            if fp == sp:
                return True

        return False
