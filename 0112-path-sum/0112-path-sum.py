# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def __init__(self):
    #     self.summ = 0
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def myfun(node, summ):
            if node == None:
                return False
            summ += node.val
            if node.left == None and node.right == None:
                if summ == targetSum:
                    return True
            return (myfun(node.left,summ) or myfun(node.right,summ))
        return myfun(root, 0)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def myfun(node):
#             if node == None:
#                 return False
#             self.summ += node.val
#             if self.summ == targetSum:
#                 return True
#             if node.left == None and node.right == None:
#                 self.summ -= node.val
#             return (myfun(node.left) or myfun(node.right))
            
#         return myfun(root)
        
        