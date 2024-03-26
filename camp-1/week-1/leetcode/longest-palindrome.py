class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_count = Counter(s)

        longez = 0
        one_used = False
        odd_used = False

        for letter in s_count:
            freq = s_count[letter]
            if freq == 1 and not one_used:
                one_used = True
            elif freq % 2 and odd_used:
                longez += freq - 1
            elif freq % 2 and not odd_used:
                longez += freq
                odd_used = True
            else:
                longez += freq
        
        if not odd_used and one_used:
            longez += 1


        return longez