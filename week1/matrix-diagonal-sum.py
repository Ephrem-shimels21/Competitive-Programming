class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        primary = 0
        secondary = 0
        n = len(mat)
        i, j  = 0, 0
        visited = set()

        while i < n and j < n:
            primary  += mat[i][j]
            visited.add((i,j))
            i += 1
            j += 1
        
        i, j = 0, n - 1

        while i < n and j >= 0:
            if (i,j) not in visited:
                secondary += mat[i][j]
            
            i += 1
            j -= 1
        
        return primary + secondary

        