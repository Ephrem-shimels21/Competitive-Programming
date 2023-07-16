class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for index,num in enumerate(nums):
            if index != 0:
                nums[index] = num + nums[index - 1]
        return nums
                