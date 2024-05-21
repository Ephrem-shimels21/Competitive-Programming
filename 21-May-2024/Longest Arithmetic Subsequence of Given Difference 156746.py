# Problem: Longest Arithmetic Subsequence of Given Difference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        dp[arr[0]] = 1

        for i in range(1, len(arr)):
            curr = arr[i] - difference
            res = dp.get(curr, 0)
            dp[arr[i]] = res + 1
        

        return max(dp.values()) 
        