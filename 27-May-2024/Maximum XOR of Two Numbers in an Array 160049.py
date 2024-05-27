# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class Trie:
    def __init__(self):
        self.children = {}
    
    def insert(self, num):
        root = self

        for i in range(31, -1, -1):
            bit = (num >> i) & 1

            if bit not in root.children:
                root.children[bit] = Trie()
            
            root = root.children[bit]
    
    def maximum_xor(self, num):
        max_xor = 0
        root = self

        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            toggled_bit = 1 - bit

            if toggled_bit in root.children:
                max_xor = (max_xor << i) | 1
                root = root.children[toggled_bit]
            
            else:
                max_xor = max_xor << 1
                root = root.children[bit]
        
        return max_xor


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_xor = 0
        mask = 0
        
        for i in range(31, -1, -1):
            mask |= (1 << i)
            prefixes = {num & mask for num in nums}
            
            current_max_xor = max_xor | (1 << i)
            for prefix in prefixes:
                if (prefix ^ current_max_xor) in prefixes:
                    max_xor = current_max_xor
                    break
        
        return max_xor
        