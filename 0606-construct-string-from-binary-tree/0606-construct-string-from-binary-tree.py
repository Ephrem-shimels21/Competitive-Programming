# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        def dfs(node):
            result = "("
            if node:
                result += str(node.val)

                if not node.left and node.right:
                    result += "()"
                result += dfs(node.left)
                result  += dfs(node.right)
                result += ")"
                return result
            else:
                return ""
        if not root.left and root.right:
            return str(root.val) + "()" + dfs(root.right)
        return str(root.val) + dfs(root.left) + dfs(root.right)
            
                
                
        
        
        