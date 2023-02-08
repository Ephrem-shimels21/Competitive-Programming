class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        window_size = n - k
        cur_sum = sum(cardPoints[:window_size])
        ans = cur_sum
        for p in range(window_size, n):
            cur_sum += cardPoints[p]
            cur_sum -= cardPoints[p - window_size]
            ans = min(cur_sum, ans)
        return sum(cardPoints) - ans
        