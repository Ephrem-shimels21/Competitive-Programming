# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def bfs(node):
            qeue = deque([node])
            visited = {node}

            while qeue:
                curr_node = qeue.popleft()
                for child in graph[curr_node]:
                    if child not in visited:
                        visited.add(child)
                        qeue.append(child)
                        node_ancestors[child].append(node)
        
           
        graph = defaultdict(list)
        node_ancestors = [[] for i in range(n)]

        for fromi, toi in edges:
            graph[fromi].append(toi)
        
        for node in range(n):
            bfs(node)
    
        return node_ancestors

        