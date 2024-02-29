class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def sum2(start, path, total):
            if total == target:
                # if path not in res:
                res.append(path[:])
                return 
          
            

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if total + candidates[i] > target:
                    break
                path.append(candidates[i])
                sum2(i + 1, path, total + candidates[i])
                path.pop()

        candidates.sort()
        res = []
        sum2(0, [], 0)

        return res
        