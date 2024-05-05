# Problem: Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        Mask = 0xFFFFFFFF
        a, b = Mask & a, b & Mask

        while b:
            carry = ((a & b) << 1) & Mask
            a, b = a ^ b, carry
        
        if a < 0x80000000:
            return a
        
        return ~(a ^ Mask)



        return a ^ b
        