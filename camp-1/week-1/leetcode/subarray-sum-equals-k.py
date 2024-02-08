class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums_count = defaultdict(int)
        prefixSums_count[0] = 1
        count = 0
        prefixSum = 0
        for num in nums:
            prefixSum += num
            count += prefixSums_count[prefixSum - k]
            prefixSums_count[prefixSum] += 1
        
        return count
