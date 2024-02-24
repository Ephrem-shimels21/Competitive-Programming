class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(set(nums))
        completes = 0

        for i in range(len(nums)):
            temp = set()
            temp.add(nums[i])
            if len(temp) == n:
                completes += 1
            for j in range(i + 1, len(nums)):
                temp.add(nums[j])
                if len(temp) == n:
                    completes += 1

        return completes
