class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        def minigetRow(row, arr, rowIndex):
            if row == 0:
                finalarr = arr
            elif row == 1:
                finalarr = [1, 1]
            else:
                finalarr = [1]
                for i in range(1, len(arr)):
                    finalarr.append(arr[i] + arr[i - 1])
                finalarr.append(1)
            if row == rowIndex:
                return finalarr
            return minigetRow(row + 1,finalarr , rowIndex)
        
        return minigetRow(0,[1], rowIndex )
        