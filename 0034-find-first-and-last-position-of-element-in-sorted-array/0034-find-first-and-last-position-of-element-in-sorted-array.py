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
            # print(initial, ending,nums[ending])
            if nums[initial] == target and nums[ending] == target:
                # print("A")
                return [initial, ending]
            elif nums[initial] != target and nums[ending] != target:
                # print("B")
                initial += 1
                ending -= 1
            elif nums[initial] != target:
                # print("C")
                initial += 1
            elif nums[ending] != target:
                # print("D")
                ending -= 1
        return [-1,-1]
        
        
        