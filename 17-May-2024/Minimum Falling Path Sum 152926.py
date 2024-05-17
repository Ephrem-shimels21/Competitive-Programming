# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        def is_bounded(row, col):
            return 0 <= row < n and 0 <= col < n

        dp = [[0] * n for _ in range(n)]
        direction = [(1, -1), (1, 0), (1, 1)]

        for i in range(n):
            dp[n - 1][i] = matrix[n - 1][i]
        
        for i in range(n - 2, -1 , -1):
            for j in range(n - 1, -1, -1):
                min_res = float("inf")
                for x, y in direction:
                    if is_bounded(x + i, y + j):
                        min_res = min(dp[x + i][y + j], min_res)
                dp[i][j] = matrix[i][j] + min_res
        
        final_min = float("inf")

        for i in range(n):
            final_min = min(final_min, dp[0][i])
        
        return final_min
        