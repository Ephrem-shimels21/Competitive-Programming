class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = n
        nums_set = set(nums)
        newNums = list(nums_set)
        newNums.sort()
        j = 0
        for index,num in enumerate(newNums):
            while j < len(newNums) and (newNums[j] < num + n):
                j += 1
            count = j - index
            ans = min(ans,n - count)
        return ans
            
        
        