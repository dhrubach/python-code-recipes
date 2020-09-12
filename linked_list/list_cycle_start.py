###############################################################
# LeetCode Problem Number : 142
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/linked-list-cycle-ii/
###############################################################

from linked_list.list_node import ListNode


class SingleLinkedList:
    def detectCycleStartNode(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None

        """ detect for cycle in the list """
        fp = sp = head
        hasCycle = False

        while fp and fp.next:
            """ move fast pointer by 2 steps """
            fp = fp.next.next

            """ move slow pointer by 1 step """
            sp = sp.next

            if fp == sp:
                hasCycle = True
                break

        if hasCycle:
            """ reset slow pointer to the beginning of the list """
            sp = head

            """ move both fast and slow pointer by 1 step till both meet
                do not reset fast pointer
                since it's a cyclic list, both will eventually meet
            """
            while fp != sp:
                fp = fp.next
                sp = sp.next

            return fp

        return None
