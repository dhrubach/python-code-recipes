###############################################################
# LeetCode Problem Number : 21
# Difficulty Level : Easy
# URL : https://leetcode.com/problems/merge-two-sorted-lists/
###############################################################
from linked_list.list_node import ListNode
from linked_list.utility import printList


class MergeSortedList:
    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            """  return None if both inputs are invalid """
            return None

        if not l1:
            """ l2 is the merged list in absense of l1 """
            return l2

        if not l2:
            """ l1 is the merged list in absense of l2 """
            return l1

        """ initialize merged list """
        dummy = ListNode()
        current = dummy

        while l1 and l2:
            """ iterate through both the list untill either reaches its end """
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next

            current = current.next

        """ copy the remainder of the other list to the merged list """
        if l1 or l2:
            current.next = l1 if l1 else l2

        return dummy.next

    def mergeRecursion(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeRecursion(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeRecursion(l1, l2.next)
            return l2


if __name__ == "__main__":
    l1 = ListNode(5, None)
    l1 = ListNode(3, l1)
    l1 = ListNode(1, l1)

    printList(l1, "sorted list 1")

    l2 = ListNode(6, None)
    l2 = ListNode(4, l2)
    l2 = ListNode(2, l2)

    printList(l2, "sorted list 2")

    sorted_list = MergeSortedList()
    printList(sorted_list.merge(l1, l2), "merged list")
