# Problem: Height Checker
(Easy) - https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        count = 0

        for idx, height in enumerate(heights):
            if height != expected[idx]:
                count += 1

        return count 