class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        clockwise = 0
        counterclockwise = 0
        temp = max(start, destination)
        start = min(start, destination)
        destination = temp

        for i in range(start, destination):
            clockwise += distance[i]
        
        for i in range(start - 1, destination - (len(distance) + 1), -1):
            counterclockwise += distance[i]

       
        
        print(clockwise, counterclockwise)
        return min(clockwise, counterclockwise)