# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def dp(idx):
            if idx == len(nums) :
                return 0

            if idx not in memo:
                value = 1
                for j in range(idx + 1, len(nums)):
                    if nums[j] > nums[idx]:
                        value = max(1 + dp(j), value)
                
                memo[idx] = value
            
            return memo[idx]

        
        memo = {}
        max_ = 0
        for i in range(len(nums)):
            max_ = max(max_, dp(i))

        return max_
        
        