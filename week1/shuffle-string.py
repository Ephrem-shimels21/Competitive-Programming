class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s_list = [0] * len(s)
        for idx, num in enumerate(indices):
            s_list[num] = s[idx]

        return "".join(s_list)