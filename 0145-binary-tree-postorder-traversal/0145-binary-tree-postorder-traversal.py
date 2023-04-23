# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root == None:
            return result
        visited = set()
        stack = [root]
        
        while stack:
            check = stack[-1]
            if check.left and check.right and check.left not in visited and check.right not in visited:
                stack.append(check.right)
                stack.append(check.left)
            elif check.right and check.right not in visited:
                stack.append(check.right)
            elif check.left and check.left not in visited:
                stack.append(check.left)
            else:
                current = stack.pop()
                result.append(current.val)
                visited.add(current)
        
        return result
        