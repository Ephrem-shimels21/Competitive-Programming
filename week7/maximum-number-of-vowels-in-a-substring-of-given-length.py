class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        v_count = 0
        max_v_count = 0
        for i in range(k):
            if s[i] in vowels:
                v_count += 1
        l = 0
        max_v_count = max(v_count, max_v_count)
        for r in range(k , len(s)):
            if s[r] in vowels:
                v_count += 1
            if s[l] in vowels:
                v_count -= 1
            l += 1
            max_v_count = max(v_count, max_v_count)
        max_v_count = max(v_count, max_v_count)
        return max_v_count
        
