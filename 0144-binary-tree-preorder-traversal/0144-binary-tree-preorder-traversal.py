# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        node_values = []
        if root == None:
            return node_values
        stack = [root]
        
        while stack:
            current = stack.pop()
            node_values.append(current.val)
            if current.right and current.left:
                stack.append(current.right)
                stack.append(current.left)
            elif current.right:
                stack.append(current.right)
            elif current.left:
                stack.append(current.left)
                
        return node_values