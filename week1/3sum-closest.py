class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = float('inf')
        nums.sort()
        for idx, num in enumerate(nums):
            l = idx + 1
            r = len(nums) - 1
            while l < r:
                total = num + nums[l] + nums[r]
                if abs(total - target) == 0:
                    return total
                elif abs(total - target) < abs(ans - target):
                    ans = total
               
                if  total == target:
                        return target
                elif  total < target:
                        l += 1
                elif total > target:
                        r -= 1
         
        return ans

      