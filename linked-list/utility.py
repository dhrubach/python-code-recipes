from list_node import ListNode
from random import randint


def printList(ln: ListNode, message: str):
    print(f"\n{message}")
    i = 0
    while ln is not None:
        print(f"value at index {i} - {ln.val}")
        ln = ln.next
        i += 1


def generateList(tail: int, items: int) -> ListNode:
    llist = ListNode(tail)

    for _ in range(items - 1):
        val = randint(2, 50)
        llist = ListNode(val, llist)

    return llist
