# Problem: Maximum Number of Fish in a Grid - https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def is_bounded(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def dfs(row, col):
            if not is_bounded(row, col):
                return 0
            
            directions  = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            result = 0
            result += grid[row][col]

            for x, y in directions:
                newx, newy = row + x, col + y
                if is_bounded(newx, newy) and (newx,newy) not in visited and grid[newx][newy] != 0:
                    visited.add((newx, newy))
                    result += dfs(newx, newy)
            
            return result

        visited = set()
        max_res = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0 and (i, j) not in visited:
                    visited.add((i, j))
                    max_res = max(dfs(i, j), max_res)
        
        return max_res


            
            
        

        