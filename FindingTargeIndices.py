class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        targetList=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                targetList.append(i)
        return targetList
        
                
