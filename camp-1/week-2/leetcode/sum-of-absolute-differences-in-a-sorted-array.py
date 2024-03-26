class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        ans = []
        total_prefixSum = sum(nums)

        prefixSum = 0

        for idx, value in enumerate(nums):

            current_sum = value * idx - prefixSum + total_prefixSum - prefixSum - (len(nums) - idx) * value

            ans.append(current_sum)
            prefixSum += value
        
        return ans
        