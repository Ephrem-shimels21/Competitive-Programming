# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        @cache
        def dp(amount, idx):
            if amount == 0:
                return 1
            
            if amount < 0:
                return 0

            result = 0
            for i in range(idx, len(coins)):
                result += dp(amount - coins[i], i)
                
            return result
        
        return dp(amount, 0)