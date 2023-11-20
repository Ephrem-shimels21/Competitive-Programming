class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix_sum = [nums[0]]
        
        min_sum = nums[0]
        
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])
            
            min_sum = min(min_sum, prefix_sum[-1])
        
        if min_sum < 0:
            return -1 * min_sum + 1
        else:
            return 1
            
        