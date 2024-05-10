# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dp(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return -1
            
            if amount in memo:
                return memo[amount]
            
            min_cost = float('inf')
            
            for coin in coins:
                res = dp(amount - coin)
                if res >= 0:
                    min_cost = min(min_cost, res + 1)
                
            memo[amount] = min_cost if min_cost != float("inf") else -1

            return memo[amount]
        
        memo = defaultdict(int)
        return dp(amount)



            
          
        
     