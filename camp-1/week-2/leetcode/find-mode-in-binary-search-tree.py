# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        modes = defaultdict(int)
        def the_mode(root):
            if not root:
                return 
            modes[root.val] += 1
            the_mode(root.left)
            the_mode(root.right)
        

        the_mode(root)
        modess = []
        for nodeVal, feq in modes.items():
            modess.append((feq, nodeVal))
        
        modess.sort(reverse = True)
        res = [modess[0][1]]
        if len(modess) == 1:
            return res
        i = 1
        while i < len(modes) and modess[i][0] == modess[0][0]:
            res.append(modess[i][1])
            i += 1
        return res