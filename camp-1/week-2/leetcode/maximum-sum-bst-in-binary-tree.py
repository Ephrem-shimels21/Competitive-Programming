# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        max_sum = 0
        def maxBSTS(root):
            nonlocal max_sum
            if not root:
                return 0, float('inf'), float('-inf'), True
            
            summL, min_left, max_left, isBSTL = maxBSTS(root.left)
            summR, min_right, max_right, isBSTR = maxBSTS(root.right)

            if  isBSTL and isBSTR and max_left < root.val and root.val < min_right:
                summ = root.val + summL + summR
                max_sum = max(summ, max_sum)
                
                max_el = max(root.val, max_right)
                min_el = min(root.val, min_left)

                return summ, min_el, max_el, True
            return 0, 0, 0, False

        maxBSTS(root)
        return max_sum
            





 
        

        