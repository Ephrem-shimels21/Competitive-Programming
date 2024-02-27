# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def sumhelper(root, prev):
            if not root.left and not root.right:
                return prev * 10 + root.val

            prev = (prev * 10) + root.val
            resl = 0
            resr = 0
            if root.left:
                resl = sumhelper(root.left, prev)
            if root.right:
                resr = sumhelper(root.right, prev)

            return resl + resr
        
        return sumhelper(root, 0)



        