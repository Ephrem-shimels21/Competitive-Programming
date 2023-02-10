# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list: List = []
 
        if not head:
            return True
        node = head
        while node != None:
            list.append(node.val)
            node = node.next
 
        if list == list[::-1]:
            return True
        else:
            return False
        