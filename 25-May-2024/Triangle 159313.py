# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        def dp(i, step):
            if step >= len(triangle):
                return 0
            if i >= len(triangle[step]):
                return 0
            
            state = (i, step)

            if state in memo:
                return memo[state]
            
            memo[state] = triangle[step][i] + min( dp(i, step + 1), dp(i + 1, step + 1))
            return memo[state]

        memo = {}
        return dp(0, 0)
            


        