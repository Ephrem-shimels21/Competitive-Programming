class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = nums[0]
        curr = 0
        for num in nums:
            if curr < 0:
                curr = 0
            curr += num
            total =  max(curr,total)
        return total
        
        
        
            
            
        