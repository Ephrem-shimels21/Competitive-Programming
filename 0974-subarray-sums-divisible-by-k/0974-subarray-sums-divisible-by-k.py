class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        
        sumCount = { 0: 1}
        prefixSum = [nums[0]]
        
        for numi in range(1,len(nums)):
            prefixSum.append(prefixSum[numi - 1] + nums[numi])
        
        for summ in prefixSum:
            if summ % k in sumCount.keys():
                count += sumCount[summ % k]
                sumCount[summ % k] += 1
            else:
                    sumCount[summ % k] = 1
    
        return count