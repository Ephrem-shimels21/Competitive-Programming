class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(len(points) - 1):
            xo, yo = points[i][0], points[i][1]
            xt, yt = points[i + 1][0], points[i + 1][1]

            ans += max(abs(xt - xo), abs(yt - yo))
        
        return ans
        
        