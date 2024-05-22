# Problem: Minimum XOR Sum of Two Arrays - https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        len2 = len(nums2)
        dp = [float('inf')] * (1 << len2)

        dp[0] = 0

        for bitmask in range(1, 1 << len2):
            idx1 = bin(bitmask).count('1') - 1
            for j in range(len2):

                if bitmask & (1 << j):
                    prev = bitmask ^ (1 << j)
                    dp[bitmask] = min(dp[bitmask], dp[prev] + (nums1[idx1] ^ nums2[j]))
        
        return dp[-1]

            