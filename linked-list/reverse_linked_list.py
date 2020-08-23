class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SingleLinkedList:
    def reverse(self, head: ListNode):
        if not head or not head.next:
            return head

        """ new head of reveresed list"""
        new_head = ListNode()
        """ pointer to current head """
        old_head = head

        while old_head.next is not None:
            """ new head is the node after the old head """
            new_head = old_head.next

            """ mvove old head pointer forward """
            old_head.next = old_head.next.next

            """ new head points to the current head """
            new_head.next = head

            """ set current head as the new head """
            head = new_head

        return head

    def reverse_v2(self, head: ListNode):
        if not head or not head.next:
            return head

        pre, cur = None, head

        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex

        return pre


def displayList(ln: ListNode):
    i = 0
    while ln is not None:
        print(f"value at index {i} - {ln.val}")
        ln = ln.next
        i += 1


if __name__ == "__main__":
    l1 = ListNode(5, None)
    l1 = ListNode(4, l1)
    l1 = ListNode(3, l1)
    l1 = ListNode(2, l1)
    l1 = ListNode(1, l1)

    print(f"original linked list")
    displayList(l1)

    print(f"\nreversed linked list")
    sll = SingleLinkedList()
    reversed_list = sll.reverse(l1)
    displayList(reversed_list)

    print(f"\nreversed linked list - version two")
    displayList(sll.reverse_v2(reversed_list))
