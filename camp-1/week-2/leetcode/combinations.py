class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1,n + 1)]
        def backtrack(start, combinations):

            if len(combinations) == k:
                ans.append(combinations[:])
                return 
            
            for j in range(start, len(nums)):
                combinations.append(nums[j])
                backtrack(j + 1, combinations)
                combinations.pop()

           
        
        ans = []
        backtrack(0, [])

        return ans

        