class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count = 0
        left = 0
        right = 0
        res = 0
        n = len(nums)

        while right < n:
            if nums[right] == 0:
                if count < k:
                    count += 1
                else:
                    while left <= right:
                        if nums[left] == 0:
                            left += 1
                            break
                        left += 1    

            L = right - left + 1
            res = max(res, L)
            right += 1

        return res
        