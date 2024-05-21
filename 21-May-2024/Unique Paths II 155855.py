# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def is_bounded(row, col):
            return 0 <= row < len(obstacleGrid) and 0 <= col < len(obstacleGrid[0])

        row  = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [[0] * col for i in range(row)]
        i = col - 1

        while obstacleGrid[row - 1][i] != 1 and i > -1:
            dp[row - 1][i] = 1
            i -= 1
                
        for i in range(row - 2 , -1, -1):
            for j in range(col - 1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    bottom = 0
                    right = 0
                    if is_bounded(i + 1, j):
                        bottom = dp[i + 1][j]
                    
                    if is_bounded(i, j + 1):
                        right = dp[i][j + 1]
        
                    dp[i][j] = right + bottom
                    
        return dp[0][0]


                    


        
        