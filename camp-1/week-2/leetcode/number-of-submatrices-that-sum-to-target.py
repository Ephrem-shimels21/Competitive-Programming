class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        prefixSum = [[0] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                top = prefixSum[r - 1][c] if r > 0 else 0
                left = prefixSum[r][c - 1] if c > 0 else 0
                top_left = prefixSum[r - 1][c - 1] if r > 0 and c > 0 else 0  
                prefixSum[r][c] = matrix[r][c] + top + left - top_left    
        res = 0
        for r1 in range(rows):
            for r2 in range(r1, rows):
                sumCount = defaultdict(int)
                sumCount[0] = 1

                for c in range(cols):
                    currSum = prefixSum[r2][c] - (prefixSum[r1 - 1][c] if r1 > 0 else 0)
                    offset = currSum - target
                    res += sumCount[offset]
                    sumCount[currSum] += 1
        
        return res

