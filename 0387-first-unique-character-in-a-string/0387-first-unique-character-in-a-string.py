class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = []
        for index,letter in enumerate(s):
            if letter not in s[index + 1:] and letter not in seen:
                return index
            else:
                seen.append(letter)
        return -1
        