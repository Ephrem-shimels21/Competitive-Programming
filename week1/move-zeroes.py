class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        holder = 0
        seeker = 0
        while seeker < len(nums):
            if nums[seeker] != 0:
                nums[holder], nums[seeker] =  nums[seeker], nums[holder]
                holder += 1
            seeker += 1

        