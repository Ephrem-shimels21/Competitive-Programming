# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []

        def find_nodes(root):
            if not root:
                return 
            find_nodes(root.left)
            nodes.append(root.val)
            find_nodes(root.right)

        find_nodes(root)

        def make_balance(nodes):
            if not nodes:
                return 
            mid = len(nodes) // 2

            new_node = TreeNode(nodes[mid])
            new_node.left = make_balance(nodes[:mid])
            new_node.right = make_balance(nodes[mid + 1: ])

            return new_node

        return make_balance(nodes)


            
        

        
            
            
        