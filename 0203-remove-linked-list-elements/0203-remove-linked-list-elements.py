# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        previous = ListNode(next = head)
        pre,current = previous, head
        
        while current:
            if current.val == val:
                pre.next = current.next
                current = current.next
            else:
                pre = current
                current = current.next
        return previous.next