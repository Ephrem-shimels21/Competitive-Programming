class Solution:
   def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return -1
        N = len(nums)
        sums = [0] * (N + 1)
        for i in range(N):
            sums[i + 1] = sums[i] + nums[i]
        for i in range(N):
            if sums[i] == sums[-1] - sums[i + 1]:
                return i
        return -1
       
                
                    
