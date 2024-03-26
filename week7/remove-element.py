class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        fast = len(nums) - 1
        # nums.sort()
        k = 0
        while slow <= fast:
            if nums[fast] == val:
                fast -= 1
                k += 1
            elif nums[slow] == val:
               nums[slow], nums[fast] = nums[fast], nums[slow]
               slow += 1
               fast -= 1
               k += 1
            else:
                slow += 1
        return len(nums) - k