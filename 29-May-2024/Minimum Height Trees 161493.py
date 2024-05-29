# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = defaultdict(list)
        degree = [0] * n
        for parent, child in edges:
            graph[parent].append(child)
            graph[child].append(parent)
            degree[parent] += 1
            degree[child] += 1
        
        qeue = deque()
        min_height_trees = []

        for i, deg in enumerate(degree):
            if deg ==  1:
                qeue.append(i)
        
    
        while qeue:
            min_height_trees.clear()

            for _ in range(len(qeue)):
                curr = qeue.popleft()
                min_height_trees.append(curr)

                for neighbor in graph[curr]:
                    degree[neighbor] -= 1

                    if degree[neighbor] == 1:
                        qeue.append(neighbor)
        
        return min_height_trees

            