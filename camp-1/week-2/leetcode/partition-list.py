# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lessthan = ListNode()
        greaterthan = ListNode()
        less = lessthan
        greater = greaterthan 

        curr = head
        while curr:
            if curr.val >= x:
                greater.next = curr
                greater = curr
            else:
                less.next = curr
                less = curr
            curr = curr.next
        less.next = greaterthan.next
        greater.next = None

        return lessthan.next
        