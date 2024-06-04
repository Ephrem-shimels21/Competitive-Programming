# Problem: Minimum Average Difference - https://leetcode.com/problems/minimum-average-difference/

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        prefix = [nums[0]]

        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
        
        min_dif, idx = float("inf"), 0

        for i in range(len(nums)):
            left_ave = (prefix[i]) // (i + 1)
            if i == len(nums) - 1:
                right_ave = 0
            else:
                right_ave = (prefix[-1] - prefix[i]) // (len(nums) - i - 1)
            
            diff = abs(left_ave - right_ave)
            
            if diff < min_dif:
                min_dif = diff
                idx = i
        
        return idx


        