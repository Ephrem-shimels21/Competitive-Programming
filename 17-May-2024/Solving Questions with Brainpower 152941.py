# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0] * len(questions)
        dp[-1] = questions[-1][0]
        base = len(questions) - 2

        for i in range(base, -1, -1):
            take = questions[i][0]
            if i + questions[i][1] + 1 < len(questions):
                take += dp[i + questions[i][1] + 1]
            
            not_take = 0
            not_take = dp[i + 1]

            dp[i] = max(take, not_take)
        
        print(dp)
        
        return max(dp)



        