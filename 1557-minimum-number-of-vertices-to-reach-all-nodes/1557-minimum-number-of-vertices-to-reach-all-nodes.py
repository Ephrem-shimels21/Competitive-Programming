class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        have_incoming = set()
        havenot_incoming = set()
        
        for edge in edges:
            node1,node2 = edge
            if node2 not in have_incoming and node1 not in havenot_incoming:
                if node2 in havenot_incoming:
                    havenot_incoming.remove(node2)
                have_incoming.add(node2)
                if node1 not in have_incoming and node1 not in havenot_incoming:
                    havenot_incoming.add(node1)
            elif node2 in havenot_incoming and node1 not in have_incoming:
                havenot_incoming.remove(node2)
                if node1 not in havenot_incoming:
                    havenot_incoming.add(node1)
                have_incoming.add(node2)
            elif node2 not in have_incoming:
                if node2 in havenot_incoming:
                    havenot_incoming.remove(node2)
                have_incoming.add(node2)
            elif node1 not in havenot_incoming:
                if node1 in have_incoming:
                    continue
                else:
                    havenot_incoming.add(node1)
        return havenot_incoming
            
        
        