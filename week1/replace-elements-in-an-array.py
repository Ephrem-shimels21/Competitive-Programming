class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        num_idx = {}

        for i in range(len(nums)):
            num_idx[nums[i]] = i

        for old, new in operations:
            idx = num_idx[old]
            num_idx[new] = num_idx.pop(old)
            nums[idx] = new

        return nums