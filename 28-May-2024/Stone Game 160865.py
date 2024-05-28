# Problem: Stone Game - https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        def dp(left, right):
            if left >= right:
                return 0
    
            state = (left, right)

            if state in memo:
                return memo[state]

            is_alice_turn = True if (right - left) % 2 != 0 else False
            leftP = piles[left] if is_alice_turn else 0
            rightp = piles[right] if is_alice_turn else 0
            
            memo[state] = max(leftP + dp(left + 1, right), rightp + dp(left, right - 1))

            return memo[state]
        
        memo = {}
        alice = dp(0, len(piles) - 1)
        return alice > (sum(piles) - alice)
        