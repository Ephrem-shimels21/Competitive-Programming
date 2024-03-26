class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candyType_count = Counter(candyType)

        n = len(candyType)

        max_candy = n // 2

        return min(max_candy, len(candyType_count))
