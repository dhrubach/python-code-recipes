###############################################################
# LeetCode Problem Number : 203
# Difficulty Level : Easy
# URL : https://leetcode.com/problems/remove-linked-list-elements/
###############################################################


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SingleLinkedList:
    def removeElements(self, head: ListNode, val: int):
        if not head:
            return

        curr = head

        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        if head.val == val:
            return head.next

        return head


def displayList(ln: ListNode):
    i = 0
    while ln is not None:
        print(f"value at index {i} - {ln.val}")
        ln = ln.next
        i += 1


if __name__ == "__main__":
    l = ListNode(5, None)
    l = ListNode(1, l)
    l = ListNode(3, l)
    l = ListNode(1, l)
    l = ListNode(1, l)
    l = ListNode(1, l)

    displayList(l)

    print("\nlist after elements removed")
    linked_list = SingleLinkedList()
    displayList(linked_list.removeElements(l, 1))

