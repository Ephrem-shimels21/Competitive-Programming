class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans, baskets, d, l, r = 0, set(), dict(), 0, 0
        while r < len(fruits):
            if fruits[r] in baskets:
                if r == 0 or fruits[r] != fruits[r - 1]:
                    d[fruits[r]] = r
                r += 1
            elif len(baskets) < 2:
                baskets.add(fruits[r])
                d[fruits[r]] = r
                r += 1
            elif len(baskets) == 2:
                baskets = set([fruits[r - 1], fruits[r]])
                l = d[fruits[r - 1]]
                d[fruits[r]] = r
            ans = max(ans, r - l)
        return ans
