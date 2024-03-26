class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[0])
        arrows = 0
        fast = len(points) - 2
        slow = len(points) - 1

        while slow >= 0:
            while fast >= 0 and points[slow][0] <= points[fast][1] and points[slow][0] >= points[fast][0]:
                fast -= 1
    
            slow = fast
            fast -= 1
            arrows += 1

        return arrows
        
