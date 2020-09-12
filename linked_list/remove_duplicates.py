###############################################################
# LeetCode Problem Number : 83
# Difficulty Level : Easy
# URL : https://leetcode.com/problems/remove-duplicates-from-sorted-list/
###############################################################

from linked_list.list_node import ListNode


class RemoveDuplicates:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            """ return head for an empty list or single node list """
            return head

        """ set the current pointer """
        curr = head

        while curr and curr.next:
            """ get the next node pointed by the current pointer """
            nex = curr.next

            if curr.val == nex.val:
                """if the values of 2 adjacent nodes are equal, skip the next node.
                set the current pointer to point at a node after the immediate next node
                """
                curr.next = nex.next
            else:
                """move the current pointer to the next node if not duplicate.
                NOTE - move the current pointer only when the values are unique
                """
                curr = curr.next

        return head
