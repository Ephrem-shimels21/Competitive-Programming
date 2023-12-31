class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        counts = [0]*max(costs)

        for cost in costs:
            counts[cost - 1] += 1
        bars = 0
       

        for cost, freq in enumerate(counts):

            if freq and coins >= cost + 1 :
                amount = coins // (cost + 1)
                coins -= min(amount,freq) * (cost + 1)
                bars += min(amount,freq)
        return bars