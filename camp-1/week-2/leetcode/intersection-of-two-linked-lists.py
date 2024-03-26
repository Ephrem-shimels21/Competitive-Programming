# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        len_A = 0
        len_B = 0
        curra = headA
        currb = headB
        while curra  or currb:
            if curra:
                curra  = curra.next
                len_A += 1
            if currb:
                currb = currb.next
                len_B += 1
        
        if len_A > len_B:
            for _ in range(len_A - len_B):
                headA = headA.next
        elif len_B > len_A:
            for _ in range(len_B - len_A):
                headB = headB.next
        
        while headA and headB and headA != headB:
            headA = headA.next
            headB = headB.next
        
        return headA
        



        