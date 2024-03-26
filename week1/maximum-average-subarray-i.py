class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start = 0
        end =  k
        summ = sum(nums[0:k])
        average = summ / k

        for end in range(k,len(nums)):
            # print(start, nums[start], end, nums[end]/)
            summ = summ - nums[start] + nums[end]
            # print(summ,summ / k)
            average = max(average, summ / k)
            # print(average)
            start += 1

        return average
            
            
            
        
        