# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        def dp(idx, is_bought):
            if idx >= len(prices):
                return 0
            
            state = (idx, is_bought)

            if state not in memo:
                if is_bought:
                    memo[state] = max(prices[idx] + dp(idx + 1, False), dp(idx + 1, is_bought))
                
                else:
                    memo[state] = max(-prices[idx] - fee + dp(idx + 1, True), dp(idx + 1, is_bought))
            
            return memo[state]

        memo = {}
        return dp(0, False)