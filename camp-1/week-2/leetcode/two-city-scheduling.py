class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        for idx, cost in enumerate(costs):
            a, b = cost
            diff = a - b
            costs[idx] = ([a, b], diff)
        costs.sort(key = lambda x : x[1])
        min_cost = 0
        n = len(costs)
        left = 0
        right = n - 1

        while left <= right:
            citaL, citb = costs[left][0]
            cita, citbR = costs[right][0]
            min_cost += citaL
            min_cost += citbR
            left += 1
            right -= 1

        return min_cost
        


      