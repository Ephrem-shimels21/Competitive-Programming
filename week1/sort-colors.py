class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0, 1, 2]
        i = 0
        for color in colors:
            for j in range(len(nums)):
                if nums[j] == color:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
        return nums
        