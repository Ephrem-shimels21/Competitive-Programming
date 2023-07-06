# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        current = head
        lefP = dummy
        if current.next == None:
            return head
        a = 1
        while a < left:
            current = current.next
            lefP  = lefP.next
            a += 1
            
        prev = None
        i = 1
        Left = None
        afterRight = None
        while  i <= (right - left + 1):
            current.next,prev,current = prev,current, current.next
         
            i += 1

       
        lefP.next.next = current
        lefP.next = prev

        return dummy.next
        
        
                
                