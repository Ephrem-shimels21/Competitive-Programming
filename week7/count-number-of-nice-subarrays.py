class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        i = res = count = 0
        for j in range(len(nums)):
            if nums[j] & 1:
                k -= 1
                count = 0
            
            while k == 0:
                k += nums[i] & 1
                i += 1
                count += 1
            res += count
        return res