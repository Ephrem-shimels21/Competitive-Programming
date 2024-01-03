class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        str_len = len(strs[0])

        for i in range(str_len):
            prev = ""
            for strr in strs:
                if prev and  strr[i] < prev:
                    count += 1
                    break
                else:
                    prev = strr[i]
        return count

        