# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def myfun(nod,val):
            if val < nod.val:
                if nod.left is None:
                    nod.left = TreeNode(val)
                else:
                    myfun(nod.left, val)
            else:
                if nod.right is None:
                    nod.right = TreeNode(val)
                else:
                    myfun(nod.right, val)
            return nod
        if root is None:
            return TreeNode(val)
    
        myfun(root, val)
        return root

              
        
        
#         def myfun(nod,val):
#             if nod.left == None:
#                 if val < nod.val:
#                     nod.left = TreeNode(val)
#             elif nod.right == None:
#                 if val > nod.val:
#                     nod.right = TreeNode(val)
                     
#             elif val < nod.val:
#                 myfun(nod.left,val)
#             elif val > nod.val:
#                 myfun(nod.right,val)
#         myfun(root,val)
#         return root