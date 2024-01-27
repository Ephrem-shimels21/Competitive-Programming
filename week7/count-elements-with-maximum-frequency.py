class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        nums_counter = Counter(nums)
        max_freq = max(nums_counter.values())
        total = 0
        count = list(nums_counter.values()).count(max_freq)
        return count * max_freq

        # for freq in nums_counter.values():
        #     if freq == max_freq
        