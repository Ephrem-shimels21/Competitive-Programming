# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        leng = 0
        curr = head
        while curr:
            curr = curr.next
            leng += 1
        capacity, extra = divmod(leng, k)
        print(capacity, extra)
        curr = head
        splits = []
            
        for j in range(k):
            part = curr
            if j < extra:
                size = capacity + 1
            else:
                size = capacity
            
            for i in range(size - 1):
                if curr:
                    curr = curr.next
            if curr:
                next_node = curr.next
                curr.next = None
                curr =  next_node
            
            splits.append(part)
        return splits
        