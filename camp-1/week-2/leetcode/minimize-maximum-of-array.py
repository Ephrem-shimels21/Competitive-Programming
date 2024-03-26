class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        max_num = nums[0]
        total = nums[0]

        for i in range(1, len(nums)):
            total += nums[i]
            curr = ceil(total / (i + 1))
            max_num = max(curr, max_num)

        return max_num
        