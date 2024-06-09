# Problem: Shuffle the Array - https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []

        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i + n])
        return ans
        