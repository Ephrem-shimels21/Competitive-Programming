class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx = 0

        count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                maxx = max(count, maxx)
                count = 0
        maxx = max(count, maxx)
        return maxx


            
        