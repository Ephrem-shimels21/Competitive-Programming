class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        mat_diagonal = defaultdict(list)
      

        for m in range(len(mat)):
            for n in range(len(mat[0])):
                mat_diagonal[m + n].append(mat[m][n])
        
        res = []

        for diagonal in mat_diagonal.items():
            if (diagonal[0] % 2) == 0:
                res.extend(diagonal[1][::-1])
            else:
                res.extend(diagonal[1])
        return res
        # reverse = False
        # for key in mat_diagonal:
        #     if not reverse:
        #         res.extend(mat_diagonal[key])
        #         if key != 0 and key % 2 != 0:
        #             reverse = True
        #     else:
        #         res.extend(mat_diagonal[key][::-1])
        #         reverse = False
        # return res
        
