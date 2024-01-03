class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        fast = 1
        slow = 0
        while fast < len(nums):
            while fast < len(nums) and  nums[fast] == nums[slow]:
                nums.remove(nums[fast])
            slow += 1
            fast += 1
        
        return len(nums)