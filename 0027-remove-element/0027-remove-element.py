class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        back = len(nums) - 1
        slow = 0
        k = len(nums)
        while slow != len(nums):
            if nums[slow] == val:
                if nums[back] != val:
                    nums[slow],nums[back] = nums[back],nums[slow]
                    nums[back] = '_'
                    slow += 1
                    back -= 1
                    k -= 1 
                elif nums[back] == val:
                    nums[back] = '_'
                    back -= 1
                    k -= 1
            elif nums[slow] != val:
                slow += 1
    
        return k 
            
        