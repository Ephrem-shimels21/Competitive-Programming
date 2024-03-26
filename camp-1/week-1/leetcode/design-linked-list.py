class Node:
    def __init__(self, val = 0, next = None):
        self.val = val 
        self.next = next

class MyLinkedList:

    def __init__(self):
        dummy_node = Node()
        self.head = dummy_node
        self.length = 0
    
    def get_node(self, index):
        if index > self.length:
            return None
        curr = self.head
        while curr and index >= 0:
            curr = curr.next
            index -= 1
        return curr
        

    def get(self, index: int) -> int:
        the_node = self.get_node(index)
        if the_node:
            return the_node.val
        return -1

        

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        temp = self.head.next
        self.head.next = new_node
        new_node.next = temp
        self.length += 1

        

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        self.length += 1
                
        
    def addAtIndex(self, index: int, val: int) -> None:
        new_node = Node(val)
        if index == self.length:
            self.addAtTail(val)
        elif index > self.length:
            pass
        else:
            the_before = self.get_node(index - 1)
            the_after = the_before.next
            the_before.next = new_node
            new_node.next = the_after
            self.length += 1


    def deleteAtIndex(self, index: int) -> None:
        node_before = self.get_node(index - 1)
        if node_before and node_before.next:
            node_next = node_before.next.next
            node_before.next = node_next
            self.length -= 1

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)