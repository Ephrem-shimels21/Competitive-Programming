# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        map_ = defaultdict(list)
        def findver(root, row, col):
            if not root:
                return 
            map_[col].append((row,root.val))

            findver(root.left, row + 1, col - 1)
            findver(root.right, row + 1, col + 1)
        
        findver(root, 0, 0)
        res = []
        for key, arr in map_.items():
            arr.sort(key = lambda x : (x[0], x[1]))
            res.append((key, arr))
        res.sort()
        ans = []
        for result in res:
            values = result[1]
            temp = []
            for value in values:
                temp.append(value[1])
            ans.append(temp)
        
        return ans
