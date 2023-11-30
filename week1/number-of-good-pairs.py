class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num_count = {}
        good_pairs = 0
        for num in nums:
            num_count[num]  = 1 + num_count.get(num, 0)

        for num in num_count:
            freq = num_count[num]
            good_pairs += freq * (freq - 1)// 2
        return good_pairs
