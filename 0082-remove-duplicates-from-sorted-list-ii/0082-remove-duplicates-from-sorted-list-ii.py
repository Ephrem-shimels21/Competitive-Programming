# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = pointer = ListNode(-101, head)
        move = head
        while move and move.next:
            if pointer.val != move.val and move.val != move.next.val:
                pointer.next = move
                pointer = pointer.next
            else:
                while move.next and move.next.val == move.val:
                    move = move.next
            move = move.next 
        pointer.next = move
        return res.next
        