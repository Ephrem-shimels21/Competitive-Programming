"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root == None:
            return 0
        max_depth = 0
        stack = deque([(root,1)])
        
        while stack:
            node,depth = stack.pop()
            max_depth = max(max_depth,depth)
            children =  node.children
            for child in children:
                stack.append((child,depth + 1))
        return max_depth
        
            
            
            
        
        