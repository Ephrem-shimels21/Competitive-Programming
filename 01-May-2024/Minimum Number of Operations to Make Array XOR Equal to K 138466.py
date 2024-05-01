# Problem: Minimum Number of Operations to Make Array XOR Equal to K - https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums_xor = nums[0]

        for num in nums[1:]:
            nums_xor ^= num
        
        res = nums_xor ^ k

        return res.bit_count()