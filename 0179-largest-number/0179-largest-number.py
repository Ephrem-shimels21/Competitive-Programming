from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # nums_str = "".join(nums)
        # nums_list = nums_str.split()
        # print(nums_list)
        nums_list = [str(num) for num in nums]
        nums_list.sort(key=cmp_to_key(self.comparing_func))
        
        return str(int("".join(nums_list)))
        
        
    
    def comparing_func(self,num1, num2):
        if num1 + num2 > num2 + num1:
            return -10
        elif num1 + num2 < num2 + num1:
            return 10
        else:
            return 0