###############################################################
# LeetCode Problem Number : 328
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/odd-even-linked-list/
###############################################################

from list_node import ListNode
from utility import generateList, printList


class SingleLinkedList:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        curr = head
        """ pointer to even elements in the list """
        eptr = ListNode()
        
        """ pointer to odd elements in the list """
        odd = optr = ListNode()

        while curr and curr.next:
            """ set the next elements in the 'even' and 'odd' lists  """
            eptr.next = curr
            optr.next = curr.next

            """ move current pointer by 2 nodes """
            curr = curr.next.next

            """ move the respective 'even' and 'odd' pointers """
            eptr = eptr.next
            optr = optr.next

        if curr:
            """ in case of even elements in the list, add last element
                to the even list
            """
            eptr.next = curr
            eptr = eptr.next

        optr.next = None
        
        """ merge the 2 list into 1 """
        eptr.next = odd.next

        return head

    def oddEvenList_v2(self, head: ListNode) -> ListNode:
        if not head:
            return None

        odd = head
        even = head.next
        evenHead = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = evenHead
        return head


if __name__ == "__main__":
    l = generateList(10, 7)

    printList(l, "input linked list")

    linked_list = SingleLinkedList()
    printList(linked_list.oddEvenList(l), "odd-even list")
