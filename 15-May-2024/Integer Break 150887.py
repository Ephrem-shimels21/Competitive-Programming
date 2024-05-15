# Problem: Integer Break - https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:

        def dp(amount):
            if amount <= 0:
                return 1
            
            if amount not in memo:
                result = 1
                for num in candidates:
                    if amount - num >= 0:
                        result =  max(result, dp(amount - num) * num)
                
                memo[amount] = result
            
            return memo[amount]
        
        memo = {}
        candidates = [i for i in range(1, n)]
        return dp(n)
        

