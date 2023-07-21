class Solution(object):
    def maxSumRangeQuery(self, nums, requests):
        """
        :type nums: List[int]
        :type requests: List[List[int]]
        :rtype: int
        """
        counts = [0] * len(nums)
        outPut = 0
        
        for request in requests:
            counts[request[0]] += 1
            if request[1] < len(nums) - 1:
                counts[request[1] + 1] -= 1
        
        for index in range(1,len(counts)):
            counts[index] = counts[index - 1] + counts[index]
        
        
        counts.sort(reverse = True)
        nums.sort(reverse = True)
        
        for i in range(len(nums)):
            outPut += counts[i] * nums[i]
        
        return outPut %  ((10 ** 9) + 7)
        
        
        