# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def db(idx, target):
            if target <= 0 or idx >= len(nums):
                return target == 0
            
            state = (idx, target)

            if state not in memo:
                memo[state] = db(idx + 1, target - nums[idx]) or db(idx + 1, target)
            
            return memo[state]
        

        memo = defaultdict(bool)

        return sum(nums) % 2 == 0 and db(0, sum(nums) // 2)
        