class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        count = 0
        for num in range(left, right + 1):
            for start, end in ranges:
                if num >= start and num <= end:
                    count += 1
                    break
        if count == right - left + 1:
            return True
        return False

        