# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return 
        visited = set()

        while head and  head.next not in visited:
            visited.add(head)
            head = head.next
        
        if not head:
            return 
        return head.next