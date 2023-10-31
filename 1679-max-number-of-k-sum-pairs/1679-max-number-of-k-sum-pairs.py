class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        max_operation = 0
        nums_dict = {}
        
        for num in nums:
            if k - num in nums_dict:
                nums_dict[k - num] -= 1
                if nums_dict[k - num] == 0:
                    nums_dict.pop(k - num)
                max_operation += 1
            else:
                nums_dict[num] = 1 + nums_dict.get(num, 0)
        return max_operation
        
       
        