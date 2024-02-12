# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
            
        prev  = None
        curr = None
        while head and head.next:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        
        head.next = curr

        return head

        