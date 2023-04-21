# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        
        while current:
            if current.next:
                if current.val == current.next.val:
                    current.next = current.next.next
            if current.next:
                if current.val == current.next.val:
                    current = current
                else:
                    current = current.next
            else:
                current = current.next
        return head
            
        