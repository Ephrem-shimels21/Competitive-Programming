class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for x , y in points:
            heap.append([x**2 + y**2,x,y])
        heapq.heapify(heap)
        closestPoints=[]
        while k > 0:
            distance,x,y = heapq.heappop(heap)
            closestPoints.append([x,y])
            k -=1
        return closestPoints