# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = []
        current = head
        
        while True:
            if current == None or current.next == None:
                return False
            visited.append(current)
            
            if current.next == None:
                return False
            if current.next in visited:
                return True
            current = current.next
            
            
       
        
        
            
        
        