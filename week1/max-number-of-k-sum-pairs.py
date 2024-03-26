class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_operation = 0
        l, r = 0, len(nums) - 1

        while l < r:
            if nums[l] + nums[r] == k:
                max_operation += 1
                l += 1
                r -= 1
            
            elif nums[l] + nums[r] > k:
                r -= 1
            elif nums[l] + nums[r] < k:
                l += 1
        
        return max_operation

        