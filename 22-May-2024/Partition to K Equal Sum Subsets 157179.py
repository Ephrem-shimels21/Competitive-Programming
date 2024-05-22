# Problem: Partition to K Equal Sum Subsets - https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        memo = {} 
        
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        target_sum = total_sum // k


        def search(used, current_sum, k_remaining):
            if k_remaining == 0:
                return True
            if current_sum == target_sum:
                return search(used, 0, k_remaining - 1)
            if used in memo:
                return memo[used]
            
            for i in range(n):
                if not (used & (1 << i)) and current_sum + nums[i] <= target_sum:
                    if search(used | (1 << i), current_sum + nums[i], k_remaining):
                        memo[used] = True
                        return True
            
            memo[used] = False
            return False

        return search(0, 0, k)