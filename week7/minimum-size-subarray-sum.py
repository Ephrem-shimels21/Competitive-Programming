class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        start = 0
        total = 0
        for end in range(len(nums)):
           total += nums[end]
           while total >= target:
               min_len = min(min_len, end - start + 1)
               total -= nums[start]
               start += 1
        
        if min_len == float('inf'):
            return 0
        return min_len
