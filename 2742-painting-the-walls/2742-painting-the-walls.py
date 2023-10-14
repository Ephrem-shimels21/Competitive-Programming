class Solution(object):
    def paintWalls(self, cost, time):
        """
        :type cost: List[int]
        :type time: List[int]
        :rtype: int
        """
        n = len(cost)
        memory = {}
        
        def dp(i,remain):
            if remain <= 0:
                return 0
            if i == n:
                return float('inf')
            if (i,remain) in memory:
                return memory[(i,remain)]
            else:
                memory[(i,remain)] = min(cost[i] + dp(i + 1, remain - 1 - time[i]),dp(i + 1,remain))
                return min(cost[i] + dp(i + 1, remain - 1 - time[i]),dp(i + 1,remain))
            
        return dp(0,n)
       
        