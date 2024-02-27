# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        qeue = deque([root.left, root.right])
        while qeue:
            left = qeue.popleft()
            right = qeue.popleft()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            
            qeue.append(right.right)
            qeue.append(left.left)
            qeue.append(left.right)
            qeue.append(right.left)

        return True