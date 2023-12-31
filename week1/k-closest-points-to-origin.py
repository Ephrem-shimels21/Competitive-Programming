class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        for idx,point in enumerate(points):
            x, y = point
            points[idx] = ([x,y],x ** 2 + y ** 2)

        
        points.sort(key = lambda x : x[1])

        ans = [point[0] for point in points[:k]]

        return ans
        