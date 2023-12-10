class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        j = len(nums) - 1
        i = j - 2

        while i >= 0:
            if sum(nums[i:j]) > nums[j]:
                return sum(nums[i : j + 1])
            else:
                i -= 1
                j -= 1
        return 0