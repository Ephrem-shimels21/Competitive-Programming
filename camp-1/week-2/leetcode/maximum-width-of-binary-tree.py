# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxWidth = float('-inf')
        def findwidth(qeue):
            nonlocal maxWidth
            if not qeue:
                return 
            ans =  qeue[-1][0] - qeue[0][0] + 1
            maxWidth = max(ans, maxWidth)
            newqeue = deque()
            while qeue:
                idx, node = qeue.popleft()
                if node.left:
                    newidx = 2 * idx
                    newqeue.append((newidx, node.left))
                if node.right:
                    newidx = 2 * idx + 1
                    newqeue.append((newidx, node.right))
            findwidth(newqeue)
        
        qeue = deque()
        qeue.append((1, root))
        findwidth(qeue)

        return maxWidth
