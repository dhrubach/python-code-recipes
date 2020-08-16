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
        """
            Add a node of value 'val' before the first element of the linked list. 
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
        """
            Append a node of value 'val' to the last element of the linked list.
        """
        self.node = {"data": val, "next": None}

        if self.head == None:
            self.head = self.tail = self.node
        else:
            curr_tail = self.tail
            self.tail = self.node
            curr_tail["next"] = self.tail

    def addAtIndex(self, index: int, val: int) -> None:
        """
            Add a node of value 'val' before the index-th node in the linked list. 
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
        """
            Delete the index-th node in the linked list, if the index is valid.
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
                break

            curr = curr["next"]

    def toString(self) -> None:

        if self.head == None:
            print(f"linked list is empty")
            return

        curr = self.head
        i = 0

        while curr["next"] != None:
            i += 1
            print(f"value at node {i} - {curr['data']}")
            curr = curr["next"]

        i += 1
        print(f"value at tail node - {curr['data']}")
        print(f"total number of nodes in the linked list - {i}")


if __name__ == "__main__":
    linked_list = SingleLinkedList()
    linked_list.addAtHead(30)
    linked_list.addAtHead(20)
    linked_list.addAtHead(10)
    linked_list.addAtTail(40)

    linked_list.toString()

    linked_list.deleteAtIndex(1)
    linked_list.toString()

    linked_list.addAtIndex(1, 20)
    linked_list.toString()

    print(f"{linked_list.get(1)}")
    print(f"{linked_list.get(10)}")
