class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        newMatrix = []
        oldMatrix = []
        
        for row in mat:
            for num in row:
                oldMatrix.append(num)
                
        numOfRows = len(mat)
        numOfColoumns = 0
        
        for ele in mat:
            numOfColoumns += len(ele)
        if r * c !=  numOfRows * len(mat[0]):
            return mat
            
        if r == numOfRows and numOfColoumns == c:
            return mat
        
        j = 0
        for i in range(r):
            newMatrix.append([])
        
        for row in newMatrix:
            while len(row) < c:
                row.append(oldMatrix[j])
                j += 1
                
        return newMatrix
               
                
                
        
        
       
        
        
        
        
            
            
        