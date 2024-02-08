class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix_sum = [nums[0]]

        for i in range(1, len(nums)):
            prefix_sum.append(nums[i] + prefix_sum[i - 1])
        
        print(prefix_sum)
        for idx, summ in enumerate(prefix_sum):
            left = summ - nums[idx]
            right = prefix_sum[-1] - summ
            if left == right:
                return idx
        
        return -1
        