# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def is_bounded(row, col):
            return 0 <= row < m and 0 <= col < n

        def dp(row, col):
            if not is_bounded(row, col):
                return 0
            if row == m - 1 and col == n - 1:
                return 1
            
            state = (row, col)

            if state not in memo:
                result = dp(row + 1, col) + dp(row, col + 1)
                memo[state] = result
            
            return memo[state]
        

        memo = {}
        return dp(0, 0)


            

        