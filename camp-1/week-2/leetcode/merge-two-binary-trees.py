# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def merge(root1, root2):
            if not root1 and not root2:
                return None
            if root1 and root2:
                res = root1.val + root2.val
                node = TreeNode(val = res)
                node.left = merge(root1.left, root2.left)
                node.right = merge(root1.right, root2.right)
                return node
            elif root1:
                return root1
            elif root2:
                return root2            
           
        


        return merge(root1, root2)