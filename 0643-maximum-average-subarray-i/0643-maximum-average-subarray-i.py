class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start = 0
        end = start + k
        average = float('-inf')
        summ = sum(nums[0:k])
        
        if len(nums) == 1:
            return float(nums[0])
        
        while end < len(nums) + 1:
            ave = summ / k
            if start == 0:
                average = max(average,ave)
            else:
                summ = (summ - nums[start - 1] + nums[end - 1])
                ave = summ / k
                average = max(average,ave)
            start += 1
            end += 1
        return average
            
            
            
        
        