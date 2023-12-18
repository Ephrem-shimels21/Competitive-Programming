class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        s_list = list(s)
        for i in range(0, n, 2 * k):
            s_list[i: i + k] = reversed(s_list[i :i + k])
        return "".join(s_list)