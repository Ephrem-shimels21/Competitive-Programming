class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        stack = deque([(0,0)])
        visited = set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def DFS(self,initial):
            stack_in = deque([initial])
            area = 1
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            while stack_in:
                x,y = stack_in.pop()
                visited.add((x,y))
                for x1,y1 in directions:
                    if min(x + x1,y + y1) < 0 or x + x1 >= len(grid) or y + y1 >= len(grid[0]):
                        continue
                    elif grid[x + x1][y + y1] == 0 and (x + x1,y + y1) not in visited and (x + x1,y + y1) not in stack:
                        stack.append((x + x1, y + y1))
                    elif grid[x + x1][y + y1] == 1 and (x + x1,y + y1) not in visited and (x + x1,y + y1) not in stack_in:
                        stack_in.append((x + x1, y + y1))
                        area += 1
                    else:
                        continue
            return area
        
        island_areas = 0
        while stack:
            a,b = stack.pop()
            if grid[a][b] == 0:
                visited.add((a,b))
                for x1,y1 in directions:
                    if min(a + x1,b + y1) < 0 or a + x1 >= len(grid) or b + y1 >= len(grid[0]):
                        continue
                    elif (a + x1,b + y1) not in visited and (a + x1,b + y1) not in stack:
                        stack.append((a + x1, b + y1))
            elif grid[a][b] == 1:
                area_i = DFS(self,(a,b))
                for x1,y1 in directions:
                    if min(a + x1,b + y1) < 0 or a + x1 >= len(grid) or b + y1 >= len(grid[0]):
                        continue
                    elif (a + x1,b + y1) not in visited and (a + x1,b + y1) not in stack:
                        stack.append((a + x1, b + y1))
                island_areas = max(island_areas,area_i)
        
        return island_areas
                
        
        
        
            
            
            
        