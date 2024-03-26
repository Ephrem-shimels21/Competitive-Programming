# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def findmax(root):
            while root.right:
                root = root.right
            return root.val
        def findmin(root):
            while root.left:
                root = root.left
            return root.val
        

        def checkValid(root, min_range, max_range):
            if not root:
                return True
            if root.val < min_range or root.val > max_range:
                return False
            
            left = checkValid(root.left, min_range, root.val - 1)
            right = checkValid(root.right, root.val + 1, max_range)

            return left and right
            

            
        min_, max_ = findmin(root), findmax(root)
        return checkValid(root, min_, max_)
            
            


        