# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        left = ListNode()
        right = ListNode()
        leftend = left
        rightend = right
        while head:
            if head.val < x:
                leftend.next = head
                leftend = head
            elif head.val >= x:
                rightend.next = head
                rightend = head
            head = head.next
        
        leftend.next = right.next
        rightend.next = None
        return left.next
        