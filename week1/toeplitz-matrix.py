class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        possible_starts = [(0,0)]

        for _ in range(m - 1):
            pre = possible_starts[-1]
            possible_starts.append((pre[0] + 1, pre[1]))

        possible_starts.append((0,0))
        for _ in range(n - 1):
            pre = possible_starts[-1]
            possible_starts.append((pre[0], pre[1] + 1))
        
        possible_starts.pop(m)

        for start in possible_starts:
            i, j = start[0], start[1]
            previous = matrix[i][j]
            while i < m and j < n:
                cur = matrix[i][j]
                if cur != previous:
                    return False
                i, j = i + 1, j + 1
        return True

       
        
            
            
        