class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        m = len(arr)
        limit = m / 4
        frequency = {}

        for num in arr:
            frequency[num] = 1 + frequency.get(num, 0)
            if frequency[num] > limit:
                return num
            