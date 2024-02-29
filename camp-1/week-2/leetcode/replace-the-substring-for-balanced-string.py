class Solution:
    def balancedString(self, s: str) -> int:
        s_count = Counter(s)
        n = len(s)
        min_len = len(s)

        if all(freq <= n // 4 for freq in s_count.values()):
            return 0
        
        idx = 0

        for i, chara in enumerate(s):
            s_count[chara] -= 1

            while idx <= i and all(occ <= n // 4 for occ in s_count.values()):
                min_len = min(min_len, i - idx + 1)
                s_count[s[idx]] += 1
                idx += 1

        return min_len 

        