class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def combineSum(path):
            if sum(path) == target:
                res.append(path[:])
                return
            elif sum(path) > target:
                return
            
            for i in range(len(candidates)):
                if (not path) or (path and candidates.index(path[-1]) <= i):
                    path.append(candidates[i])
                    combineSum(path)
                    path.pop()
               

        

        res = []
        combineSum([])
        return res
        