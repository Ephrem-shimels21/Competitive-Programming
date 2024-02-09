class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x :x[2])
        n = trips[-1][2]
        total_passangers = [0] * (n + 2)
        for numPassengers, fromi, toi in trips:
            total_passangers[fromi] += numPassengers
            total_passangers[toi] -= numPassengers
            if numPassengers > capacity:
                return False
        
        for i in range(1, len(total_passangers)):
            prefix_sum = total_passangers[i - 1] + total_passangers[i]
            if prefix_sum > capacity:
                return False
            total_passangers[i] = prefix_sum
        return True
        