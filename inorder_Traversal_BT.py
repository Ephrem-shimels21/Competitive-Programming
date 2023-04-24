class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def __init__(self):
        self.result = []
    def inorderTraversal(self, root):
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
        # visited = []
        # stack = [root]
        # while stack:
        #     check = stack[-1]
        #     if check.left and check.left not in visited:
        #         stack.append(check.left)
        #     else:
        #         current = stack.pop()
        #         visited.append(current)
        #         self.result.append(current.val)
        #         if current.right:
        #             stack.append(current.right)
        # return self.result


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(3)
e = TreeNode(4)
f = TreeNode(5)
g = TreeNode(6)
h = TreeNode(7)
i = TreeNode(8)
j = TreeNode(9)
k = TreeNode(10)
a.left = c
a.right = b
b.left = d
b.right = e
e.left = None
e.right = None
f.left = None
f.right = None
c.left = f
c.right = g
d.left = h
d.right = i
g.left = j
g.right = k

ob = Solution()
print(ob.inorderTraversal(a))

