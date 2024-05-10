# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def dp(idx, is_bought, is_selled):
            if idx >= len(prices):
                return 0
            
            state = (idx, is_bought, is_selled)

            if state not in memo:
                if is_selled:
                    memo[state] = dp(idx + 1, is_bought, False)
                elif is_bought:
                    memo[state] = max(prices[idx] + dp(idx + 1, False, True), dp(idx + 1, is_bought, is_selled))
            
                else:
                    memo[state] = max(-prices[idx]  + dp(idx + 1, True, is_selled), dp(idx + 1, is_bought, is_selled))
            
            return memo[state]

        memo = {}
        return dp(0, False, False)
        