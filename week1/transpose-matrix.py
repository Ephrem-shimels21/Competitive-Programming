class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = [[None] * len(matrix) for _ in range(len(matrix[0]))] 
        for r,row in enumerate(matrix):
            for col, val in enumerate(row):
                result[col][r] = val
        return result