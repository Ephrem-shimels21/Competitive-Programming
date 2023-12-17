class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_length = 1
        if not nums:
            return 0
        for num in nums:
            if num - 1 not in nums_set and num + 1 in nums_set:
                length = 0
                temp = num
                while temp in nums_set:
                    length += 1
                    temp += 1
                max_length = max(length, max_length)    
        return max_length    