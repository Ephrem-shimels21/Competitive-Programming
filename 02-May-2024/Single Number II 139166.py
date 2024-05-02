# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0

        for num in nums:
            ones = (num ^ ones) & (~twos)
            twos = (num ^ twos) & (~ones)

        return ones     
        