class Solution:
    def minimizedStringLength(self, s: str) -> int:
        s_set = set(s)
        return len(s_set)
        