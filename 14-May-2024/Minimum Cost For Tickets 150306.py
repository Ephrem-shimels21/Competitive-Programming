# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        def dp(idx):
            if idx >= len(days):
                return 0
            
            if idx not in memo:
                min_ele = float("inf")       
                for cost, duration in zip(costs, [1, 7, 30]):
                    next_idx = bisect_left(days, duration + days[idx])
                    totalCost = cost + dp(next_idx)
                    min_ele = min(min_ele, totalCost)

                memo[idx] = min_ele
            
            return memo[idx]
            
        
        memo = {}
        return dp(0)

        