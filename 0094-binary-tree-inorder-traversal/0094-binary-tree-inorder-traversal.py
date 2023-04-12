# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def __init__(self):
        self.result = []
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # if root == None:
        #     return
        # self.inorderTraversal(root.left)
        # self.result.append(root.val)
        # self.inorderTraversal(root.right)
        # return self.result
        if root == None:
            return self.result
        stack = [root]
        visited = []
        
        # print(stack[-1].right)
        while stack:
            # break
            check = stack[-1]
            if check.left and check.left not in visited:
                stack.append(check.left)
            else:
                current = stack.pop()
                visited.append(current)
                self.result.append(current.val)
                if current.right:
                    stack.append(current.right)
        return self.result
                
                
        
        
        