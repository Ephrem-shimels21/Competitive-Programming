class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 0
        j = 1
        
        while j < len(prices):
            if prices[i] >= prices[j]:
                profit = max(prices[j] - prices[i],profit)
                i  = j
                j += 1
                
            else:
                profit = max(prices[j] - prices[i],profit)
                j += 1
                
        return profit
        
            
                
        