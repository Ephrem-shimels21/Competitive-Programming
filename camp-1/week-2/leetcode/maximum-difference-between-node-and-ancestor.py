# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def findminmax(root, max_, min_):
            if not root:
                return max_ - min_
            
            max_ = max(root.val, max_)
            min_ = min(root.val, min_)
            
            left = findminmax(root.left, max_, min_)
            right = findminmax(root.right, max_, min_)

            return max(left, right)
        

        return findminmax(root, root.val, root.val)


            