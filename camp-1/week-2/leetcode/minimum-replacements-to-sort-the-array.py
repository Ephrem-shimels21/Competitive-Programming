class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        operations = 0
        no_spaces = float('inf')
        value = float('inf')
        right = len(nums) - 2

        while right > 0 and nums[right] <= nums[right + 1]:
            right -= 1
        if nums[right] > nums[right + 1]:
            no_spaces = math.ceil(nums[right] / nums[right + 1])
            value = nums[right] // no_spaces
            right -= 1
            operations += no_spaces - 1
        while right >= 0:
            if nums[right] > value:
                no_spaces = math.ceil(nums[right] / value)
                value = nums[right] // no_spaces
                operations += no_spaces - 1
            else:
                value = nums[right]
            right -= 1

        
        return operations
            
            


