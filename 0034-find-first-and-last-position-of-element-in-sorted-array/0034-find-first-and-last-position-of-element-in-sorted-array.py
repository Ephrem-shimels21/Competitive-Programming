class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        initial = 0
        ending = len(nums) - 1
        
        while initial <= ending:
            if nums[initial] == target and nums[ending] == target:
                return [initial, ending]
            elif nums[initial] != target and nums[ending] != target:
                initial += 1
                ending -= 1
            elif nums[initial] != target:
                initial += 1
            elif nums[ending] != target:
                ending -= 1
        return [-1,-1]
        
        
        
