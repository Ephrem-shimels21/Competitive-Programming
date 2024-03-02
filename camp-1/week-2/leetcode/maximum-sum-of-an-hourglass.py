class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = float('-inf')
        
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                current_hourglass = grid[i][j] + grid[i - 1][j - 1] + grid[i - 1][j] + grid[i - 1][j + 1] + grid[i + 1][j - 1] + grid[i + 1][j] + grid[i + 1][j + 1]
                ans = max(current_hourglass, ans)
        
        return ans
