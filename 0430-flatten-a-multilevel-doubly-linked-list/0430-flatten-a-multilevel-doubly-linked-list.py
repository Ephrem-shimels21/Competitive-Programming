"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return 
        stack = deque([head])
        dummy = Node(0)
        
        curr = dummy
        
        while stack:
            curr_node = stack.pop()
            
            if curr_node.next:
                stack.append(curr_node.next)
                
            if curr_node.child:
                stack.append(curr_node.child)
                curr_node.child = None
                
            curr_node.prev = curr
            curr.next = curr_node
            curr = curr_node
        
        dummy.next.prev = None
        
        return dummy.next
        
                
                