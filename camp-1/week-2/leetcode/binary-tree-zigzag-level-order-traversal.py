# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        def movezig(qeue, level):
            if not qeue:
                return 
            next_ = deque()
            values = []
            if  level % 2 == 0:
                while qeue:
                    node = qeue.popleft()
                    if not node:
                        return
                    if node.left:
                        next_.append(node.left)
                    if node.right:
                        next_.append(node.right)
                    values.append(node.val)
            else:
                while qeue:
                    node = qeue.pop()
                    if not node:
                        return 
                    if node.right:
                        next_.appendleft(node.right)
                    if node.left:
                        next_.appendleft(node.left)
                    values.append(node.val)
            ans.append(values)
            movezig(next_, level + 1)
        
        start = deque()
        if root:
            start.append(root)

        movezig(start, 0)

        return ans


            

        