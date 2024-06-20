# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        edgeToEdge = dict()
        max_edge_node = 0
        
        for edge in edges:
            node1,node2 = edge
            if node1 in edgeToEdge.keys() and node2 in edgeToEdge.keys():
                edgeToEdge[node1] += 1
                edgeToEdge[node2] += 1
            elif node1 not in edgeToEdge.keys()  and node2 not in edgeToEdge.keys():
                edgeToEdge[node1] = 1
                edgeToEdge[node2] = 1
            elif node1 in edgeToEdge.keys():
                edgeToEdge[node1] += 1
            elif node2 in edgeToEdge.keys():
                edgeToEdge[node2] += 1
            elif node1 not in edgeToEdge.keys():
                edgeToEdge[node1] = 1
            elif node2 not in edgeToEdge.keys():
                edgeToEdge[node2] = 1
            
        for node in edgeToEdge.keys():
            if edgeToEdge[node] > max_edge_node:
                max_edge_node = node
        return max_edge_node
        
            
        