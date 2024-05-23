# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp = {stone: set() for stone in stones}
        dp[0].add(1)
        if stones[1] != 1:
            return False
        
        dp[1].add(1)
    

        for stone in stones[1:]:
            for k in dp[stone]:
                if k - 1 > 0 and stone + k - 1 in dp:
                    dp[stone + k - 1].add(k - 1)
                
                if stone + k in dp:
                    dp[stone + k ].add(k)
                
                if stone + k + 1 in dp:
                    dp[stone + k + 1].add(k + 1)
            
    
        return len(dp[stones[-1]]) > 0