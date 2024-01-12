class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l = 0
        max_consc_T = 0
        wind = defaultdict(int)
        for r in range(len(answerKey)):
            wind[answerKey[r]] += 1
            while wind["F"] > k:
                wind[answerKey[l]] -= 1
                if wind[answerKey[l]] == 0:
                    wind.pop(answerKey[l])
                l += 1
            max_consc_T = max(max_consc_T, r - l + 1)
        max_consc_T = max(max_consc_T, r - l + 1)

        l = 0
        max_consc_F = 0
        wind = defaultdict(int)
        for r in range(len(answerKey)):
            wind[answerKey[r]] += 1
            while wind["T"] > k:
                wind[answerKey[l]] -= 1
                if wind[answerKey[l]] == 0:
                    wind.pop(answerKey[l])
                l += 1
            max_consc_F = max(max_consc_F, r - l + 1)
        max_consc_F = max(max_consc_F, r - l + 1)

        return max(max_consc_T, max_consc_F)
        