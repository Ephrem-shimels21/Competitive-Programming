# Problem: IPO - https://leetcode.com/problems/ipo/

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        candidate_profits = []
        candidate_capitals = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(candidate_capitals)
        maximized_capital = w

        for _ in range(k + 1):
            if candidate_profits:
                maximized_capital += -heapq.heappop(candidate_profits)[0]

            
            while candidate_capitals and candidate_capitals[0][0] <= maximized_capital:
                c, p = heapq.heappop(candidate_capitals)
                heapq.heappush(candidate_profits, (-p, c))
            
        
        return maximized_capital
            
