# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        i = len(nums) - 3
        j = len(nums) - 1


        while i >= 0:
            if nums[i] + nums[i + 1] > nums[j]:
                return sum(nums[i : j + 1])
            i -= 1
            j -= 1
        
        return 0
