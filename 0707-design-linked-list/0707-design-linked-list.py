class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        # self.myfun()
        if index > self.length - 1:
            return -1
        else:
            current = self.head
            i = 0
            while i < index:
                current = current.next
                i += 1
        return current.val


    def addAtHead(self, val: int) -> None:
        new = Node(val)       
        if self.length == 0:
            self.head = new
            self.length += 1
        else:
            current = self.head
            self.head = new
            self.head.next = current
            self.length += 1

        

    def addAtTail(self, val: int) -> None:
        if self.length == 0:
            self.addAtHead(val)
        else:
            new = Node(val)
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new
            self.length += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        # print(self.length)        
        if (self.length == 0 and index == 0 ) or (index == 0) :
            self.addAtHead(val)
            
        elif index == self.length:
            self.addAtTail(val)         
        elif index < self.length:
            new = Node(val)
            current = self.head
            i = 0
            while i < index - 1:
                current = current.next
                i += 1
            the_next = current.next
            current.next = new
            new.next = the_next
            self.length += 1
        

    def deleteAtIndex(self, index: int) -> None:
        current = self.head
        if index == 0:
            if current.next:
                self.head =  current.next
                self.length -= 1
            else:
                self.head = None
                self.length -= 1

        else:
            if index <= self.length - 1:
                i = 0
                while i < index - 1:
                    current = current.next
                    i += 1
                if self.length == 1:
                    self.head = None
                    self.length  -= 1
                else:
                    the_next = current.next.next
                    current.next = the_next
                    self.length -= 1
                # print(current.val)
                
    def myfun(self):
        i = 0
        current = self.head
        while i < self.length:
            # print(i,current.val)
            current = current.next
            i += 1
        
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)