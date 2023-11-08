class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        
        for index, num in enumerate(nums):
            summ = num
            i = index + 1
            while i < len(nums):
                summ += nums[i]
                j = i + 1
                k = len(nums) - 1
                while j < k:
                    if summ + nums[j] + nums[k] ==  target:
                        if [num,nums[i], nums[j], nums[k]] not in res:
                            res.append([num, nums[i], nums[j], nums[k]])
                        j += 1
                    elif summ + nums[j] + nums[k] < target:
                        j += 1
                    
                    elif summ + nums[j] + nums[k] > target:
                        k -= 1
                i += 1
                summ = num
        return res
                    
                    
                    
        
        