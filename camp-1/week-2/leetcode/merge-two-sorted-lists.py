# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyhead = ListNode()
        curr = dummyhead
        def minimerge(list1, list2, curr):       
            if not list1 and not list2:
                return 
            
            if not list1 and list2:
                curr.next = list2
                curr = curr.next
                minimerge(list1,list2.next, curr)
            elif not list2 and  list1:
                curr.next = list1
                curr = curr.next
                minimerge(list1.next, list2, curr)
            
            if list1 and list2 and list1.val <= list2.val:
                curr.next = list1
                curr = curr.next
                minimerge(list1.next, list2, curr)
            elif list1 and list2 and list2.val < list1.val:
                curr.next = list2
                curr = curr.next
                minimerge(list2.next, list1, curr)
        
        minimerge(list1, list2, curr)

        return dummyhead.next

        