# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def dp(transaction, idx, is_bought):
            if idx >= len(prices) or transaction == 0:
                return 0
            
            state = (transaction, idx, is_bought)

            if state not in memo:
                if is_bought:
                    memo[state] = max(prices[idx] + dp(0, idx + 1, False), dp(transaction, idx + 1, is_bought))
                
                else:
                    memo[state] = max(-prices[idx] + dp(transaction, idx + 1, True), dp(transaction, idx + 1, is_bought))
            
            return memo[state]

        memo = {}
        return dp(1, 0, False)
