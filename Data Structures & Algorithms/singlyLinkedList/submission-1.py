class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

class LinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if not self.head or index < 0:
            return -1

        i = 0
        curr = self.head
        while curr:
            if i == index:
                return curr.value
            curr = curr.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        new = Node(val)
        if not self.head:
            self.head = new
        else:
            new.next = self.head
            self.head = new

    def insertTail(self, val: int) -> None:
        new = Node(val)
        if not self.head:
            self.head = new
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new

    def remove(self, index: int) -> bool:
        if not self.head:
            return False

        if index == 0:
            self.head = self.head.next
            return True

        curr = self.head
        i = 0
        while curr and i < index - 1:
            curr = curr.next
            i += 1
        
        if not curr or not curr.next:
            return False

        curr.next = curr.next.next
        return True
        
    def getValues(self) -> List[int]:
        res = []
        curr = self.head

        while curr:
            res.append(curr.value)
            curr = curr.next

        return res
