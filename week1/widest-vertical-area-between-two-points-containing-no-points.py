class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[0])
        max_sum = 0

        for i in range(len(points) - 1):
            max_sum = max(max_sum, points[i + 1][0] - points[i][0])
        
        return max_sum
        




        