# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def db(idx, total):
            if idx == len(nums) and total == target:
                return 1

            if idx >= len(nums):
                return 0
            
            state = (idx, total)

            if state not in memo:
                memo[state] = db(idx + 1, total + nums[idx]) + db(idx + 1, total - nums[idx])
            
            return memo[state]
        
        memo = defaultdict(int)
        return db(0, 0)
