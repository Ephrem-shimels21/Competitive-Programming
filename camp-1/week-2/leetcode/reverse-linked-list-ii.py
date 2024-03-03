# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
       
        curr = 1
        dummy = ListNode(next = head)
        previous = dummy
        node = head
        while curr  < left:
            previous = node
            node = node.next
            curr += 1
        

        prev = None
        current = None
        move = node
        
        while curr <= right:
            current = move
            move = move.next
            current.next = prev
            prev = current
            curr += 1

        node.next = move
        previous.next = current
       

        return dummy.next



            


        


        