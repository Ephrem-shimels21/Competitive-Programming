class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        hi = len(nums) - 1
        lo = 0
        mid = (hi + lo) // 2
        
        while True:
            if lo == hi == mid:
                if nums[mid] < target:
                    return mid + 1
                elif nums[mid] > target:
                    if mid != 0:
                        return mid
                    else:
                        return 0
                elif nums[mid] == target:
                    return mid
            elif target < nums[mid]:
                if hi == mid:
                    hi = mid - 1
                else:
                    hi = mid
                mid = (hi + lo) // 2
            elif target > nums[mid]:
                if lo == mid:
                    lo = mid + 1
                else:
                    lo = mid
                mid = (hi + lo) // 2
            elif target == nums[mid]:
                return mid
           
                
                
        