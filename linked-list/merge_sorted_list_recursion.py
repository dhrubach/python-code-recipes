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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

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
    displayList(sorted_list.mergeTwoLists(l1, l2))