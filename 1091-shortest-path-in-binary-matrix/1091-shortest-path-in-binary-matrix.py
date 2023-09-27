class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        qeue = deque([(0,0,1)])
        visited = set((0,0))
        directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
        while qeue:
            row,col,length = qeue.popleft()
            if min(row,col) < 0 or max(row,col) >= len(grid) or grid[row][col]:
                continue     
            if (row == len(grid) - 1 and col == len(grid) - 1) :
                return length
            
            for (x,y) in directions:
                if (row + x, col + y) not in visited:
                    qeue.append((row + x, col + y,length + 1))
                    visited.add((row + x, col + y))
        return -1
            
            
        
        
        