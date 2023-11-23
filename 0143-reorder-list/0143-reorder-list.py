# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        current = head
        while current:
            temp = current.next
            current.next = None
            stack.append(current)
            current = temp
     
        current = stack.pop(0)
        is_end = True
        while stack:
            if not is_end:
                current.next = stack.pop(0)
                current = current.next
                is_end = True
            elif is_end:
                current.next = stack.pop()
                current = current.next
                is_end = False
                
        return head
        
            
            
        