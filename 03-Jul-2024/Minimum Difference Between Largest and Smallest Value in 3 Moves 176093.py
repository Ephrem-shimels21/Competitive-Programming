# Problem: Minimum Difference Between Largest and Smallest Value in 3 Moves - https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 5:
            return 0
        
        nums.sort()
        ans = float('inf')

        for i in range(4):
            r = 3 - i
            ans = min(ans, nums[n - 1 - r] - nums[i])
        
        return ans


        

