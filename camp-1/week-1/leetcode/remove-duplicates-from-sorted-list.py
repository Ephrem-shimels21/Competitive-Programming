# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            while curr.next and curr.val == curr.next.val:
                temp = curr.next
                curr.next = temp.next
            if curr.next:
                curr = curr.next
        return head
