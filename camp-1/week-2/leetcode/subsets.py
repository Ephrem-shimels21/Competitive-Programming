class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def findsubsets(idx, subsets):
            if len(subsets) == len(nums):
                return 

            for i in range(idx, len(nums)):
                subsets.append(nums[i])
                ans.append(subsets[:])
                findsubsets(i + 1, subsets)
                subsets.pop()
        

        ans = [[]]
        findsubsets(0, [])
        return ans
        