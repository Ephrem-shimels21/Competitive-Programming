class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = -1
        l = 0
        r = len(nums) - 1
        mid = (l + r) // 2

        while l <= r:
            if nums[mid] == target:
                start = mid  
                r = mid - 1
                mid = (l + r) // 2
            elif nums[mid] > target:
                r = mid - 1
                mid = (l + r) // 2
        
            elif nums[mid] < target:
                l = mid + 1
                mid = (l + r) // 2
        l = 0
        r = len(nums) - 1
        mid = (l + r) // 2
        end = -1

        while l <= r:
            if nums[mid] == target:
                end = mid  
                l = mid + 1
                mid = (l + r) // 2
            elif nums[mid] > target:
                r = mid - 1
                mid = (l + r) // 2
        
            elif nums[mid] < target:
                l = mid + 1
                mid = (l + r) // 2
        return [start, end]
        

        
