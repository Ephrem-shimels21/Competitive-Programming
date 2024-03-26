class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixSums_count = defaultdict(int)
        prefixSums_count[0] = 1

        count = 0
        prefix_sum = 0
        for bit in nums:
            prefix_sum += bit
            count += prefixSums_count[prefix_sum - goal]

            prefixSums_count[prefix_sum] += 1
        
        return count

            