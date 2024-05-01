# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        binary_num = bin(num)[2:]
        length = len(binary_num)
        num_ones = 2 ** length - 1

        return num ^ num_ones

