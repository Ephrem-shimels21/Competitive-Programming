class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        k = r

        while l <= r:
            mid = (l + r) // 2
            currtime = 0
            for pile in piles:
                if pile <= mid:
                    currtime += 1
                else:
                    currtime += ceil(pile / mid)
            
            if currtime <= h:
                k = min(mid, k)
                r = mid - 1
            else:
                l = mid + 1
        
        return k
        