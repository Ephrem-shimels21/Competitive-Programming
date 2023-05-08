class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        for index in range(len(prices) - 1):
            if prices[index] < prices[index + 1]:
                profit += prices[index + 1] - prices[index]
            
        return profit
        
        