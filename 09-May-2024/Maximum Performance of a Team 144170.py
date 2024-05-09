# Problem: Maximum Performance of a Team - https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        mod = 10 ** 9 + 7
        performance = sorted(zip(efficiency, speed), reverse = True)
        total_performance = 0
        heap = []
        max_performance = 0

        for idx in range(n):
            effi, spe = performance[idx]
            total_performance += spe
            max_performance = max(max_performance, total_performance * effi)

            if idx < k - 1:
                heappush(heap, spe)
            
            elif heap and heap[0] < spe:
                total_performance -= heappop(heap)
                heappush(heap, spe)
            
            else:
                total_performance -= spe
        
        return max_performance % mod
