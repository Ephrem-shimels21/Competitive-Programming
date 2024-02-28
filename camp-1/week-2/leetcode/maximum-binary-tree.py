# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def constructor(nums):
            if not nums:
                return None
            idx = 0
            maxe = -1
            for i in range(len(nums)):
                if nums[i] > maxe:
                    maxe = nums[i]
                    idx = i
            
            node = TreeNode(maxe)
            node.left = constructor(nums[:idx])
            node.right = constructor(nums[idx + 1:])
            return node
        
        return constructor(nums)
        