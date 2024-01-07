class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for index, num in enumerate(nums):
                a = num
                left = index + 1
                right = len(nums) - 1
                summ = num
                while left < right:
                    if  summ + nums[left] + nums[right] == 0:
                        temp = [num, nums[left], nums[right]]
                        if temp not in result:
                            result.append(temp)
                        left +=  1
                    elif  summ + nums[left] + nums[right] < 0:
                        left += 1
                    
                    elif summ + nums[left] + nums[right] > 0:
                        right -= 1
        
        return result 
                        
                        
                
            
            
        