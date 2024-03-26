class Solution:
    def findMin(self, nums: List[int]) -> int:
        _min = float("inf")
        l = 0
        r = len(nums) - 1
        mid = (l + r) // 2

        while l <= r:
            if nums[r] > nums[l]:
                return min(_min,nums[l])
            elif nums[mid] >= nums[l]:
                _min = min(_min, nums[mid])
                l = mid + 1
                mid = (l + r) // 2
            elif nums[mid] < nums[l]:
                _min = min(_min, nums[mid])
                r = mid - 1
                mid = (l + r) // 2
        return _min




        