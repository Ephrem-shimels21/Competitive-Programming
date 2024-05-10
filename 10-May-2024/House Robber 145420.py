# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def db(idx):
            if idx == 0:
                return nums[0]
            
            elif idx == 1:
                return max(nums[0], nums[1])
            
            if idx not in memo:
                memo[idx] = max(db(idx - 1), nums[idx] + db(idx - 2))
            
            return memo[idx]
        
        memo = {}
        return db(len(nums) - 1)

        