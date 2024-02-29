class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [i for i in range(1, 10)]


        def sum3(start, path, total):
            if total == n and len(path) == k:
                res.append(path[:])
                return 
            
            if len(path) > k:
                return 
            
            for i in range(start, len(nums)):
                if len(path) > k:
                    break
                path.append(nums[i])
                sum3(i + 1, path, total + nums[i])
                path.pop()

        res = []
        sum3(0, [], 0)
        return res
        