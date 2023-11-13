class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        w = len(grid[0])
        
        movements = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = set()
        no_islands = 0
        
        def bfs(r, c):
            qeue = deque()
            visited.add((r,c))
            qeue.append((r,c))
            
            while qeue:
                x, y = qeue.popleft()
                if (x,y) not in visited:
                    visited.add((x,y))
                for a, b in movements:
                    if x + a  in range(n) and  y + b in range(w) and grid[x + a][y + b] == "1" and (x + a,y + b) not in visited:
                        qeue.append((x + a,y + b))
                        visited.add((x + a,y + b))

        for r in range(n):
            for c in range(w):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    no_islands += 1
                    
        return no_islands
                
        