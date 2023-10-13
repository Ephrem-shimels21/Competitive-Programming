class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        ans = float('inf')
        dp = [cost[0],cost[1]]
        
        if len(cost) == 2:
            return min(cost[0],cost[1])
        
        for i in range(2,len(cost)):
            dp.append(min(dp[i - 1],dp[i - 2]) + cost[i])
            ans = min(dp[i],dp[i - 1])
        return ans
        
        
        