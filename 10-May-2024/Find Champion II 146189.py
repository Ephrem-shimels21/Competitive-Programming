# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        losers = set()

        for team1, team2 in edges:
            graph[team1].append(team2)
            losers.add(team2)
        
        winners = set()

        for i in range(n):
            if i not in losers:
                winners.add(i)
        
        if len(winners) > 1:
            return -1
        return winners.pop()
        