# Problem: Palindrome Partitioning II - https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [[True] * n for _ in range(n)]
        
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
        
        cuts = [i for i in range(n)]
    
        for i in range(1, n):
            for j in range(i + 1):
                if dp[j][i]:
                    cuts[i] = min(cuts[i], 0 if j == 0 else 1 + cuts[j - 1])
        
        return cuts[-1]


        