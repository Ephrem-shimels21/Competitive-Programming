class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if nums[0] + nums[1] <= nums[-1]:
            return "none"
        nums_set = set(nums)
        if len(nums_set) == 1:
            return "equilateral"
        
        elif len(nums_set) == 2:
            return "isosceles"
        
        elif len(nums_set) == 3:
            return "scalene"

        