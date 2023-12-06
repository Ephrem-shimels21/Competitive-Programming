class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        first = set("qwertyuiop")
        second = set("asdfghjkl")
        third = set("zxcvbnm")
        for word in words:
            f, s, t = 0, 0, 0
            for letter in word:
                if letter.lower() in first:
                    f += 1
                elif letter.lower() in second:
                    s += 1
                else:
                    t += 1
            if f == len(word) or s == len(word) or t == len(word):
                ans.append(word)
        return ans
        