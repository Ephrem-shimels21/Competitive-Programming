# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        newHead = ListNode()
        curr = newHead

        while head1 or head2:
            if head1 and head2 :
                if head1.val <= head2.val:
                    curr.next = head1
                    curr = curr.next
                    head1 = head1.next
                else:
                    curr.next = head2
                    curr = curr.next
                    head2 = head2.next
               
            else:
                while head1:
                    curr.next = head1
                    curr = curr.next
                    head1 = head1.next
                
                while head2:
                    curr.next = head2
                    curr = curr.next
                    head2 = head2.next
        
        return newHead.next

                
        