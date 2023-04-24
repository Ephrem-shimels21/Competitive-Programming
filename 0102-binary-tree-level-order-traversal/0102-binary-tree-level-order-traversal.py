# import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root == None:
            return result
        result.append([root.val])
        stack = [root]
        
        while stack:
            temp = []
            level_nodes = []
            while stack:
                current = stack.pop(0)
                if current.left and current.right:
                    temp.append(current.left.val)
                    temp.append(current.right.val)
                    level_nodes.append(current.left)
                    level_nodes.append(current.right)
                    
                elif current.right:
                    temp.append(current.right.val)
                    level_nodes.append(current.right)
                elif current.left:
                    temp.append(current.left.val)
                    level_nodes.append(current.left)
            if temp:
                result.append(temp)
            for node in level_nodes:
                stack.append(node)
                
        return result
                
            
        