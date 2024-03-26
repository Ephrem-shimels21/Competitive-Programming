class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.row = len(self.matrix)
        self.col = len(self.matrix[0])
        self.matrix_prefix_sum = self.matrix
        self.matrix_prefix_sum = [[0] * self.col] + self.matrix_prefix_sum
        for i in range(self.row + 1):
            self.matrix_prefix_sum[i] = [0] + self.matrix_prefix_sum[i]
      
        for i in range(1,self.row + 1):
            for j in range(1, self.col + 1):
                self.matrix_prefix_sum[i][j] = self.matrix_prefix_sum[i][j - 1] + self.matrix_prefix_sum[i - 1][j] + self.matrix[i - 1][j - 1] - self.matrix_prefix_sum[i - 1][j - 1]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        return self.matrix_prefix_sum[row2 + 1][col2 + 1] - self.matrix_prefix_sum[row1][col2 + 1] - self.matrix_prefix_sum[row2 + 1][col1] + self.matrix_prefix_sum[row1][col1]
        



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)