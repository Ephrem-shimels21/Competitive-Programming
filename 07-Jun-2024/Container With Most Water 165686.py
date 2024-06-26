# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        area = 0
        while left <= right:
            area = max(area,(right - left) * min(height[left],height[right]))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return area