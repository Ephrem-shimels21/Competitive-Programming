class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        col_max = defaultdict(int)
        row_max = defaultdict(int)

        for r in range(len(grid)):
            _max = 0
            for c in range(len(grid[0])):
                _max = max(_max, grid[r][c])
            row_max[r] = _max
        
        for c in range(len(grid[0])):
            _maxc = 0
            for r in range(len(grid)):
                _maxc = max(grid[r][c], _maxc)
            col_max[c] = _maxc
        
    
        
        max_sum = 0
        for i in range(len(grid)):
            maxr = row_max[i]
            for j in range(len(grid[0])):
                maxc = col_max[j]
                max_sum += min(maxc, maxr) - grid[i][j]
        return max_sum

        