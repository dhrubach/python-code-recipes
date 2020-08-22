###############################################################
# LeetCode Problem Number : 21
# Difficulty Level : Easy
# URL : https://leetcode.com/problems/merge-two-sorted-lists/
###############################################################

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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


def displayList(ln: ListNode):
    i = 0
    while ln is not None:
        print(f"value at index {i} - {ln.val}")
        ln = ln.next
        i += 1


if __name__ == "__main__":
    l1 = ListNode(5, None)
    l1 = ListNode(3, l1)
    l1 = ListNode(1, l1)

    print('sorted list 1')
    displayList(l1)
    
    l2 = ListNode(6, None)
    l2 = ListNode(4, l2)
    l2 = ListNode(2, l2)

    print('\nsorted list 2')
    displayList(l2)
    
    print('\nmerged list')
    sorted_list = MergeSortedList()
    displayList(sorted_list.merge(l1, l2))