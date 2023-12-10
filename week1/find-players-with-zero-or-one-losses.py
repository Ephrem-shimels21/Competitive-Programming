class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        no_win_lose = {}
        no_lose = {}

        for player1, player2 in matches:
            win = no_win_lose.get(player1, [0, 0])
            win[0] += 1
            lose = no_win_lose.get(player2, [0,0])
            lose[1] += 1 
            no_win_lose[player1] = win
            no_win_lose[player2] = lose 
                 
        not_lost = []
        lost_one = []
        for player in no_win_lose:
            if no_win_lose[player][1] == 0:
                not_lost.append(player)
            
            elif no_win_lose[player][1] == 1:
                lost_one.append(player)
        
        not_lost.sort()
        lost_one.sort()

        return [not_lost, lost_one]

        print(no_win_lose) 
        