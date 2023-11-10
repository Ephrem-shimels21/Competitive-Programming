class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        difference = []
        summ = 0
        index = 0
        for a, b in costs:
            difference.append((index, b - a))
            index += 1
        
        
        difference.sort(key = lambda x : x[1])
        
        j = 0
        k = len(costs) - 1
        
        while j < k:
            summ += costs[difference[j][0]][1]
            summ += costs[difference[k][0]][0]
            j += 1
            k -= 1
        
        return summ
            
            