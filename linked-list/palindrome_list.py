###############################################################
# LeetCode Problem Number : 234
# Difficulty Level : Easy
# URL : https://leetcode.com/problems/palindrome-linked-list/
###############################################################

from list_node import ListNode
from utility import printList


class SingleLinkedList:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            """ check for empty list or a list with 1 element """
            return True

        if not head.next.next:
            """ check for a list with 2 elements """
            return head.val == head.next.val

        """ split the list into 2 equal halves"""
        lhalf, rhalf = self.splitList(head)
        
        """ reverse the right-half of the list """
        rhalf = self.reverseList(rhalf)

        while lhalf and rhalf:
            if lhalf.val != rhalf.val:
                """ return False anytime there is a mismatch """
                return False
            lhalf = lhalf.next
            rhalf = rhalf.next

        """ input linked list is a palindrome """
        return True

    def splitList(self, head: ListNode) -> ():
        lh, rh = head, None
        p = q = lh

        while True:
            p = p.next.next

            if not p.next or not p.next.next:
                rh = q.next.next

                if not p.next:
                    q.next = None
                    break

                if not p.next.next:
                    q.next.next = None
                    break

            q = q.next
        
        return (lh, rh)

    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur = None, head

        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex

        return pre
        
    
if __name__ == "__main__":
    l = ListNode("2", None)
    l = ListNode("3", l)
    l = ListNode("5", l)
    l = ListNode("3", l)
    l = ListNode("2", l)

    printList(l, "original list")

    linked_list = SingleLinkedList()
    print(f"\nisPalindrome - {linked_list.isPalindrome(l)}")
