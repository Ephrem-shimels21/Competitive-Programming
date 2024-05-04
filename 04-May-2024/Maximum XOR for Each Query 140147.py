# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        comulative = reduce(xor, nums)
        mask = (1 << maximumBit) - 1
        result = []

        for num in nums[::-1]:
            result.append(comulative ^ mask)
            comulative ^= num
        
        return result
        
        
