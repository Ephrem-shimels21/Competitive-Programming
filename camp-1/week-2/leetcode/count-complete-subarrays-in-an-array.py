class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        whole_distinct = defaultdict(int)

        for num in nums:
            whole_distinct[num] += 1
        
        subarr_distinct = defaultdict(int)
        completes = 0
        l = 0

        for idx,num in enumerate(nums):
            subarr_distinct[num] += 1
            while len(subarr_distinct) == len(whole_distinct):
                completes += len(nums) - idx
                subarr_distinct[nums[l]] -= 1
                if subarr_distinct[nums[l]] == 0:
                    subarr_distinct.pop(nums[l])
                l += 1

        
        return completes



        