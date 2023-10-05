# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        dummy_node = ListNode()
        dummy_node.next = head
        left = dummy_node
        right = head
        for _ in range(n):
            right = right.next
        
        while right != None:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return dummy_node.next
        
        
        
        
        
        
        
        
        
        
        
        

            
            
        