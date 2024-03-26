class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        new_nums = list(filter(lambda x : x != 0, nums))
        if len(new_nums) < 1:
            return 0
        l = 0
        r = len(new_nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if new_nums[mid] <= 0:
                l = mid + 1
            else:
                r = mid - 1
        
        if new_nums[mid] < 0:
            neg = mid + 1
            pos = len(new_nums) - mid - 1
        else:
            pos = len(new_nums) - mid 
            neg = mid 
        
        return max(pos, neg)

        