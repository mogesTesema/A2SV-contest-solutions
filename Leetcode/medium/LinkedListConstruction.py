class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        temp = self.head
        counter = 0
        while temp:
            if counter == index:
                return temp.val
            counter += 1
            temp = temp.next
        return -1

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if not self.head:
            self.addAtHead(val)
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            self.addAtHead(val)
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return
        if index > self.size:
            return

        node = Node(val)
        temp = self.head
        counter = 0

        while counter < index - 1 and temp:
            temp = temp.next
            counter += 1
        
        if temp is None:
            return

        node.next = temp.next
        temp.next = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if self.head is None or index < 0 or index >= self.size:
            return

        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return

        temp = self.head
        counter = 0

        while counter < index - 1 and temp:
            temp = temp.next
            counter += 1
        
        if temp is None or temp.next is None:
            return

        temp.next = temp.next.next
        self.size -= 1

    def display(self):
        storage = []
        temp = self.head
        while temp:
            storage.append(temp.val)
            temp = temp.next
        print(storage)

