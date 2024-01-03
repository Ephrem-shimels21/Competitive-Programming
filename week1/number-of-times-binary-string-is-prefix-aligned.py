class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count = 0
        needed_ones = 0
        available_ones = 0

        for idx in flips:
            needed_ones = max(needed_ones,idx)
            available_ones += 1
            if available_ones == needed_ones:
                count += 1
        return count
        