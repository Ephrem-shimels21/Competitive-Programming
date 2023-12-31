class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()

        l = 0
        r = len(piles) - 2
        max_coin = 0
        while l < r:
           
            max_coin += piles[r]
            r -= 2
            l += 1
        return max_coin

