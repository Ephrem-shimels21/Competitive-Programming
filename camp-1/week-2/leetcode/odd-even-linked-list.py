# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        evendummy = ListNode()
        odddummy = ListNode()

        def group_them(even, odd, curr, idx):
            if not curr:
                even.next = None
                odd.next = None
                return 
            if idx % 2 != 0:
                odd.next = curr
                odd = odd.next
            else:
                even.next = curr
                even = even.next
            group_them(even, odd, curr.next, idx + 1)
        
        even = evendummy
        odd = odddummy
        group_them(even, odd, head, 1)
        cur_od = odddummy
        while cur_od.next:
            cur_od = cur_od.next
        cur_od.next = evendummy.next
        return odddummy.next

