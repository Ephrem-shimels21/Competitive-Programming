# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums_xor = reduce(xor, nums)
        least_sig_bit = nums_xor & -nums_xor
        unique_one = 0

        for num in nums:
            if num & least_sig_bit:
                unique_one ^= num
        
        unique_two = nums_xor ^ unique_one

        return [unique_one, unique_two]


        