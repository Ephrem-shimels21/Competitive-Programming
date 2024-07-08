# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = [i for i in range(1, n + 1)]
        qeue = deque(nums)

        while len(qeue) > 1:
            for i in range(k - 1):
                curr = qeue.popleft()
                qeue.append(curr)
            qeue.popleft()
        
        return qeue[0]
