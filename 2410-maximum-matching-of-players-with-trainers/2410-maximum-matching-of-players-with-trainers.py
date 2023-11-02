class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        p = 0
        t = 0
        output = 0
        players.sort()
        trainers.sort()
        while p < len(players) and t < len(trainers):
            if players[p] <= trainers[t]:
                output += 1
                p += 1
                t += 1
            else:
                t += 1
        return output
            
        