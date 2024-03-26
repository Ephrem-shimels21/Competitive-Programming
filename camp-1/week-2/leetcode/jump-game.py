class Solution:
    def canJump(self, nums: List[int]) -> bool:
        good = len(nums) - 1
        prev = len(nums) - 2

        if len(nums) == 1:
            return True
        
        while prev >= 0:
            if nums[prev] + prev >= good:
                good = prev
                prev -= 1
            else:
                prev -= 1
        
        return good == 0

        