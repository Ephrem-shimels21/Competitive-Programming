# Problem: Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def dp(idx1, idx2):
            if idx1 >= len(text1) or idx2 >= len(text2):
                return 0
            
            state = (idx1, idx2)

            if state not in memo:
                if text1[idx1] == text2[idx2]:
                    memo[state] = 1 + dp(idx1 + 1, idx2 + 1)
                
                else:
                    memo[state] = max(dp(idx1 + 1, idx2), dp(idx1, idx2 + 1))
            
            return memo[state]
        
        memo = {}
        return dp(0, 0)
            

    