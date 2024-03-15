class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        mid = (l + r) // 2
        minCap = float('inf')

        while l <= r:
            currcap = mid
            day = 1
            for weight in weights:
                if currcap - weight < 0:
                    day += 1
                    currcap = mid
                currcap -= weight
                
            if day <= days:
                minCap = min(minCap, mid)
                r = mid - 1
            else:
                l = mid + 1
            mid = (l + r) // 2
        
        return minCap


        