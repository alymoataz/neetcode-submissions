class LinkedList:
    
    def __init__(self, next=None, val=0):
        self.next = next
        self.val = val

    def get(self, index: int) -> int:
        if index < 0:
            return -1
        head = self.next
        for _ in range(index):
            if not head:
                return -1
            head = head.next
        return head.val if head else -1

    def insertHead(self, val: int) -> None:
        n = LinkedList(self.next, val)
        self.next = n

    def insertTail(self, val: int) -> None:
        if not self.next:
            self.insertHead(val)
            return
        curr = self.next
        while curr.next:
            curr = curr.next
        n = LinkedList(None, val)
        curr.next = n

    def remove(self, index: int) -> bool:
        if index < 0:
            return False
        prev = self
        curr = self.next
        for _ in range(index):
            if not curr:
                return False
            prev = curr
            curr = curr.next
        if not curr:
            return False
        prev.next = curr.next
        return True

    def getValues(self) -> List[int]:
        arr = []
        curr = self.next
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr