class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        widw = defaultdict(int)
        l = 0
        max_len = 0
        for r in range(len(nums)):
            widw[nums[r]] += 1

            while widw[0] > k:
                widw[nums[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
        
        return max_len
            



        