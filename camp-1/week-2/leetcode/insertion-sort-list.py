# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        prev, current = head, head.next

        while current:
            if current.val >= prev.val:
                prev = current
                current = current.next
        
            else:
                insert_at = dummy
                while  insert_at.next.val <= current.val:
                    insert_at = insert_at.next
                
                temp = current.next
                current.next = insert_at.next
                insert_at.next = current

                prev.next = temp
                current = temp

        return dummy.next


        