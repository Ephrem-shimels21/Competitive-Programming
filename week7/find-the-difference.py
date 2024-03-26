class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_count = Counter(s)
        t_count = Counter(t)

        for char in t_count:
            if char not in s_count:
                return char
            elif t_count[char] != s_count[char]:
                return char
                