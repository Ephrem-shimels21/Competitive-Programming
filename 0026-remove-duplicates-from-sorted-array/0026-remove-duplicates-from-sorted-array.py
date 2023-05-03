class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        fast = 1
        unique = len(nums)
        last = nums[-1]
        
        if len(nums) == 1:
            return 1      
                
        while fast < len(nums):
            if nums[slow] == nums[fast]:
                del nums[fast]
                # nums.append("_")
                unique -= 1
            elif nums[slow] != nums[fast]:
                slow += 1
                fast += 1
                
        return unique
        