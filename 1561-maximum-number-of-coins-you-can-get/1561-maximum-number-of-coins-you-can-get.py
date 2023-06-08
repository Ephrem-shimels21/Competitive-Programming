class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        piles.reverse()
  
        no_3s = len(piles) // 3

        i = 1
        added_coins = 1
        max_coins = 0
        while added_coins <= no_3s:
            max_coins += piles[i]
            added_coins += 1

            i += 2
        return max_coins
            
        