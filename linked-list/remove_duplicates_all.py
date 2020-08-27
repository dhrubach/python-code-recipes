############################################################################
# LeetCode Problem Number : 82
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
############################################################################

from list_node import ListNode
from utility import printList


class RemoveAllDuplicates:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            """ return head for an empty list or a single - node list """
            return head

        """ set previous and current pointers """
        prev, curr = ListNode(), head
        isDuplicate = False

        while curr:
            if curr.next and curr.val == curr.next.val:
                """ if the next node is valid and has the same value as
                    current node, skip that node
                    
                    set the duplicate flag
                    
                    keep repeating till all duplicates of a given val have been removed
                """
                isDuplicate = True
                curr.next = curr.next.next
            else:
                if isDuplicate:
                    """ point prev pointer to the node after current to remove the last
                        val of a duplicate set
                    """
                    prev.next = curr.next
                    
                    """ move head pointer if duplicates were removed from the beginning """
                    if head == curr:
                        head = prev.next
                    
                    """ move the current pointer """
                    curr = curr.next
                else:
                    """ move previous and current pointer when no duplicates """
                    prev = curr
                    curr = curr.next
                
                """  reset duplicate flag """    
                isDuplicate = False

        return head

    def deleteDuplicatesV2(self, head: ListNode) -> ListNode:
        """ alternate solution from leetcode submissions
        """
        if not head:
            return head

        dummy = pre = ListNode(0)
        dummy.next = head

        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                pre.next = head
            else:
                pre = pre.next
                head = head.next

        return dummy.next

