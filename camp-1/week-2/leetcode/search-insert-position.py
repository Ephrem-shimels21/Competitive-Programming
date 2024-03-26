class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        mid = (l + r) // 2
        targidx = 0

        while l <= r:
            if nums[mid] > target:
                r = mid - 1
                mid = (l + r) // 2
            
            elif nums[mid] < target:
                targidx = mid + 1
                l = mid + 1
                mid = (l + r) // 2
            
            else:
                return mid
        
        return targidx
        