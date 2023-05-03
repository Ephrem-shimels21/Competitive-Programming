import functools
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(left,right):
            if not left and not right:
                return True
            elif not left or not right:
                
                return False
            return (left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left))
        
        return dfs(root.left,root.right)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         inorder = []
#         visited = []
#         stack = [root]
        
#         while stack:
            
#             if stack[-1].left and stack[-1].left not in visited :
#                 stack.append(stack[-1].left)
#             else:
#                 current = stack.pop()
#                 visited.append(current)
#                 inorder.append(current.val)
#                 if current.right:
#                     stack.append(current.right)
#         print(inorder[:inorder.index(root.val)])
#         print(inorder[inorder.index(root.val) + 1:])
#         for ele in inorder[:inorder.index(root.val)]:
#             if ele not in inorder[inorder.index(root.val) + 1:]:
#                 return False
        
#         l1 = inorder[:inorder.index(root.val)]
#         l2 = inorder[inorder.index(root.val) + 1:]
#         if len(l1) == len(l2) == 0:
#             return True
#         if len(l1) == len(l2) == 1:
#             return True
        
#         if functools.reduce(lambda x, y : x and y, map(lambda p, q: p == q,l1,l2), True):
#                    return False
#         else:
#                    return True
    
                
        