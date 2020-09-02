###############################################################
# LeetCode Problem Number : 707
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/design-linked-list/
###############################################################
class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.node = None

    def get(self, index: int) -> None:
        """ Get the value of the index-th node in the linked list.

            If the index is invalid, return -1.
        """

        if self.head == None:
            return -1

        curr = self.head
        position = 0
        search_val = -1

        while curr is not None:
            if position == index:
                search_val = curr["data"]
                break
            position += 1
            curr = curr["next"]

        return search_val

    def addAtHead(self, val: int) -> None:
        """ Add a node of value 'val' before the first element of the linked list.

            After the insertion, the new node will be the first node of the linked list.
        """

        if self.head == None:
            self.node = {"data": val, "next": None}
        else:
            self.node = {"data": val, "next": self.head}

        self.head = self.node

        """
            Reset tail if this is the first node
        """
        if self.tail == None:
            self.tail = self.head

    def addAtTail(self, val: int) -> None:
        """ Append a node of value 'val' to the last element of the linked list.
        """

        self.node = {"data": val, "next": None}

        if self.head == None:
            self.head = self.tail = self.node
        else:
            curr_tail = self.tail
            self.tail = self.node
            curr_tail["next"] = self.tail

    def addAtIndex(self, index: int, val: int) -> None:
        """ Add a node of value 'val' before the index-th node in the linked list.

            If index equals to the length of linked list, the node will be appended to the end of linked list.
            If index is greater than the length, the node will not be inserted.
        """

        """ empty linked list """
        if self.head == None and index == 0:
            self.head = self.tail = {"data": val, "next": None}
            return

        """ trying to insert a node in an empty linked list """
        if self.head is None and index > 0:
            return

        """ overwrite 'head' node """
        if index == 0:
            self.head["data"] = val
            return

        curr = self.head
        position = 1

        while curr is not None:
            if position == index:
                self.node = {"data": val, "next": curr["next"]}
                curr["next"] = self.node

                """ check if inserting at tail """
                if self.node["next"] is None:
                    self.tail = self.node
                break

            position += 1
            curr = curr["next"]

    def deleteAtIndex(self, index: int) -> None:
        """ Delete the index-th node in the linked list, if the index is valid.
        """

        """ empty linked list """
        if self.head == None:
            return

        """ delete the current head """
        if index == 0:
            self.head = self.head["next"]

            """ reset tail pointer if there are no nodes present """
            if self.head == None:
                self.tail = None

            return

        curr = self.head
        position = 0

        while curr["next"] is not None:
            position += 1
            if position == index:
                curr["next"] = curr["next"]["next"]

                """ check if deleting at tail """
                if curr["next"] is None:
                    self.tail = curr

                break

            curr = curr["next"]

    def toString(self) -> None:
        """ Display snapshot of current linked list along with number of nodes.

            Example :
                value at node 0 - 84
                value at node 1 - 2
                value at node 2 - 39
                value at tail node - 42
                total number of nodes in the linked list - 4
        """
        if self.head == None:
            print(f"linked list is empty")
            return

        curr = self.head
        i = 0

        while curr["next"] != None:
            print(f"value at node {i} - {curr['data']}")
            i += 1
            curr = curr["next"]

        i += 1
        print(f"value at tail node - {curr['data']}")
        print(f"total number of nodes in the linked list - {i}")

    def executeCommands(self, command: str, operands: list):
        """ Automate execution of large number of operations to test implementation.

            Not part of main linked list implementation. Wrote this function
            to simulate large input test bed
        """
        if command == "addAtHead":
            self.addAtHead(operands[0])
            return None
        elif command == "addAtTail":
            self.addAtTail(operands[0])
            return None
        elif command == "addAtIndex":
            self.addAtIndex(operands[0], operands[1])
            return None
        elif command == "deleteAtIndex":
            self.deleteAtIndex(operands[0])
        else:
            val = self.get(operands[0])
            print(val)
            return val


if __name__ == "__main__":
    linked_list = SingleLinkedList()

    commands = [
        "addAtHead",
        "addAtTail",
        "addAtTail",
        "get",
        "get",
        "addAtTail",
        "addAtIndex",
        "addAtHead",
        "addAtHead",
        "addAtTail",
        "addAtTail",
        "addAtTail",
        "addAtTail",
        "get",
        "addAtHead",
        "addAtHead",
        "addAtIndex",
        "addAtIndex",
        "addAtHead",
        "addAtTail",
        "deleteAtIndex",
        "addAtHead",
        "addAtHead",
        "addAtIndex",
        "addAtTail",
        "get",
        "addAtIndex",
        "addAtTail",
        "addAtHead",
        "addAtHead",
        "addAtIndex",
        "addAtTail",
        "addAtHead",
        "addAtHead",
        "get",
        "deleteAtIndex",
        "addAtTail",
        "addAtTail",
        "addAtHead",
        "addAtTail",
        "get",
        "deleteAtIndex",
        "addAtTail",
        "addAtHead",
        "addAtTail",
        "deleteAtIndex",
        "addAtTail",
        "deleteAtIndex",
        "addAtIndex",
        "deleteAtIndex",
        "addAtTail",
        "addAtHead",
        "addAtIndex",
        "addAtHead",
        "addAtHead",
        "get",
        "addAtHead",
        "get",
        "addAtHead",
        "deleteAtIndex",
        "get",
        "addAtHead",
        "addAtTail",
        "get",
        "addAtHead",
        "get",
        "addAtTail",
        "get",
        "addAtTail",
        "addAtHead",
        "addAtIndex",
        "addAtIndex",
        "addAtHead",
        "addAtHead",
        "deleteAtIndex",
        "get",
        "addAtHead",
        "addAtIndex",
        "addAtTail",
        "get",
        "addAtIndex",
        "get",
        "addAtIndex",
        "get",
        "addAtIndex",
        "addAtIndex",
        "addAtHead",
        "addAtHead",
        "addAtTail",
        "addAtIndex",
        "get",
        "addAtHead",
        "addAtTail",
        "addAtTail",
        "addAtHead",
        "get",
        "addAtTail",
        "addAtHead",
        "addAtTail",
        "get",
        "addAtIndex",
    ]
    inputParams = [
        [84],
        [2],
        [39],
        [3],
        [1],
        [42],
        [1, 80],
        [14],
        [1],
        [53],
        [98],
        [19],
        [12],
        [2],
        [16],
        [33],
        [4, 17],
        [6, 8],
        [37],
        [43],
        [11],
        [80],
        [31],
        [13, 23],
        [17],
        [4],
        [10, 0],
        [21],
        [73],
        [22],
        [24, 37],
        [14],
        [97],
        [8],
        [6],
        [17],
        [50],
        [28],
        [76],
        [79],
        [18],
        [30],
        [5],
        [9],
        [83],
        [3],
        [40],
        [26],
        [20, 90],
        [30],
        [40],
        [56],
        [15, 23],
        [51],
        [21],
        [26],
        [83],
        [30],
        [12],
        [8],
        [4],
        [20],
        [45],
        [10],
        [56],
        [18],
        [33],
        [2],
        [70],
        [57],
        [31, 24],
        [16, 92],
        [40],
        [23],
        [26],
        [1],
        [92],
        [3, 78],
        [42],
        [18],
        [39, 9],
        [13],
        [33, 17],
        [51],
        [18, 95],
        [18, 33],
        [80],
        [21],
        [7],
        [17, 46],
        [33],
        [60],
        [26],
        [4],
        [9],
        [45],
        [38],
        [95],
        [78],
        [54],
        [42, 86],
    ]
    result = []

    for c, p in zip(commands, inputParams):
        result.append(linked_list.executeCommands(c, p))
        print(f"{c} - {p}")
        linked_list.toString()
        print("\n")

    print(result)

