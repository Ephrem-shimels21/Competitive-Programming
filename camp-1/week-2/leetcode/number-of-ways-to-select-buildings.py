class Solution:
    def numberOfWays(self, s: str) -> int:
        valids = 0
        total0 = s.count('0')
        total1 = s.count('1')

        count1 , count0 = 0, 0

        for num in s:
            if num == "0":
                valids += (total1 - count1) * count1
                count0 += 1
            else:
                valids += (total0 - count0) * count0
                count1 += 1
        return valids