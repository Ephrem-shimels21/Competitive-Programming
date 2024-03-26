class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        min_rad = float('-inf')
        houses.sort()
        heaters.sort()

        for house in houses:
            l = 0
            r = len(heaters) - 1
            curr_min = float('inf')

            while l <= r:
                mid = (l + r) // 2
                diff = abs(heaters[mid] - house)
                curr_min = min(curr_min, diff)

                if house == heaters[mid]:
                    break
                elif house < heaters[mid]:
                    r = mid - 1
                else:
                    l = mid  + 1
                    
            min_rad = max(min_rad, curr_min)
        
        return min_rad
            
