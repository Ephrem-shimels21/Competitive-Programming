class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]

        prefix_sum = 0
        for num in nums:
            if prefix_sum < 0:
                prefix_sum = 0
            prefix_sum += num
            max_sum = max(max_sum, prefix_sum)

        
        return max_sum
