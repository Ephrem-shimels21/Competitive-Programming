class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        def backtrackDup(start, path):
            if len(path) == len(nums):
                return 
            for j in range(start, len(nums)):
                path.append(nums[j])
                if path not in subsets:
                    subsets.append(path[:])
                backtrackDup(j + 1, path)
                path.pop()

        nums.sort()
        subsets = [[]]
        backtrackDup(0, [])

      
        return subsets
        