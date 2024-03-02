class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mod_by = (10 ** 9) + 7
        queries = [0] * len(nums)

        for start, end in requests:
            queries[start] += 1
            if end + 1 < len(nums):
                queries[end + 1] -= 1
    
        for i in range(1, len(nums)):
            queries[i] = queries[i-1] + queries[i]
        
        queries.sort(reverse = True)
        nums.sort(reverse = True)

        max_sum = 0

        for a, b in zip(nums, queries):
            max_sum += a * b
            
        
        return max_sum % mod_by


        