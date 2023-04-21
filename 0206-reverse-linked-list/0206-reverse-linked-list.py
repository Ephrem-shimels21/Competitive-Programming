# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        pre = None
        while current:
            current.next,pre,current= pre,current,current.next 
        return pre
        
        
        
        
        
        
        
        
       