class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        trips.sort(key = lambda trip: trip[1])
        heap = []
        passengerCount = 0
        
        for trip in trips:
            numPassenger, start, end = trip
            
            while heap and heap[0][0] <= start:
                passengerCount -= heap[0][1]
                heapq.heappop(heap)
            
            passengerCount += numPassenger
            if passengerCount > capacity:
                return False
            
            heapq.heappush(heap, [end,numPassenger])
        return True
            
            
                

            
            
        