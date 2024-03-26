class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        sentence = text.split()
        brokenLetts = Counter(brokenLetters)
        visited = set()

        count = 0
        for word in sentence:
            for letter in word:
                if letter in brokenLetts:
                    count += 1
                    break
        return len(sentence) - count
            