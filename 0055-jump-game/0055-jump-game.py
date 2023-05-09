class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        j = len(nums) - 2
        while j >= 0:
            if nums[j] + j >= goal:
                goal = j
                j -= 1
            else:
                j -= 1
        if goal == 0:
            return True
        else:
            return False
        
        
        
        
        # if len(nums) == 1:
        #     return True
        # i = 0
        # while i < len(nums) - 1:
        #     if nums[i] == 0:
        #         return False
        #     elif nums[i] + i >= len(nums) - 1:
        #         return True
        #     j = 1
        #     k = 0
        #     temp = float('-inf')
        #     while j <= nums[i]:
        #         if nums[i + j] > temp:
        #             temp = nums[i + j]
        #             k += 1
        #         j += 1
        #     i += k
        
        