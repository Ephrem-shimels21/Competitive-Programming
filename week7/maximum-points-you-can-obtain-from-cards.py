class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        slow = 0
        max_sum = 0
        K_sum = 0
        total_sum = sum(cardPoints)
        for i in range(n - k):
            K_sum += cardPoints[i]
        
        max_sum = max(max_sum, total_sum - K_sum)
        for fast in range(n - k, n):
            K_sum += cardPoints[fast]
            K_sum -= cardPoints[slow]
            max_sum = max(max_sum, total_sum - K_sum)
            slow += 1
        return max_sum

        