class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascalTri = [[1]]
        for i in range(1,numRows):
            pascalTri.append([])
               
        
        for i in range(1,numRows):
            pascalTri[i - 1].append(0)
            pascalTri[i - 1].insert(0,0)
            j = 0
            k = 1
            print(pascalTri[i - 1])
            while k < len(pascalTri[i - 1]):
                pascalTri[i].append((pascalTri[i - 1])[j] + (pascalTri[i - 1])[k])
                j += 1
                k += 1
            pascalTri[i - 1].pop()
            pascalTri[i - 1].pop(0)
                
        return pascalTri
        