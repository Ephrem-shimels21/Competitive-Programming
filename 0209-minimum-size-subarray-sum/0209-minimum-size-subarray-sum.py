class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, end = 0, 0
        summ = 0
        minimal_length = float('inf')
        while end != len(nums):
            summ += nums[end]
            if nums[end] == target:
                return 1
            while summ >= target:
                minimal_length = min(minimal_length,end - start + 1)
                summ -= nums[start]
                start += 1
            end += 1
           
        
        if minimal_length == float("inf"):
            return 0
        return minimal_length

            