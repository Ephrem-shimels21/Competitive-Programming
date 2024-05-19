# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s, t):
        m, n = len(s), len(t)
        
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        for j in range(n + 1):
            dp[0][j] = True
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        
        return dp[m][n]



            