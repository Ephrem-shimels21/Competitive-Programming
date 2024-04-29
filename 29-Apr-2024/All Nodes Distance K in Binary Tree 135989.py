# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def find_parent(node, parent):
            if node:
                parents[node] = parent
                find_parent(node.left, node)
                find_parent(node.right, node)
        
        def find_nodes_at_k(node, distance):
            if not node or node.val in visited:
                return 
            
            visited.add(node.val)

            if distance == 0:
                output.append(node.val)
            
            else:
                find_nodes_at_k(node.left, distance - 1)
                find_nodes_at_k(node.right, distance - 1)
                find_nodes_at_k(parents[node], distance - 1)
        
        parents = {}
        visited = set()
        output = []

        find_parent(root, None)
        find_nodes_at_k(target, k)

        return output