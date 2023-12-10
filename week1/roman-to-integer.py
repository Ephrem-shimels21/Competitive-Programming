class Solution:
    def romanToInt(self, s: str) -> int:
        roman_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C" : 100, "D" : 500, "M": 1000}
        placed_before = "IXC"
        placed_after = "VLDXCM"
        sub_values = (4, 9, 40, 90, 400, 900)

        if len(s)  == 1:
            return roman_int[s[0]]

        integer = roman_int[s[0]]
        i = 1

        while i < len(s):
            if s[i - 1] in placed_before and s[i] in placed_after and roman_int[s[i]] - roman_int[s[i - 1]] in sub_values:
                integer -= roman_int[s[i - 1]]
                integer += roman_int[s[i]] - roman_int[s[i - 1]]
            else:
                integer += roman_int[s[i]]
            i += 1
        return integer

        



        