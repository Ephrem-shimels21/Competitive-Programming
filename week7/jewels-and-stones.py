class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # jewels_count = Counter(jewels)
        stones_count = Counter(stones)

        total = 0

        for jewel in jewels:
            total += stones_count[jewel]
        return total
        