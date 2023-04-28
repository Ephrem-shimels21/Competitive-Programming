class Solution:
    def romanToInt(self, s: str) -> int:
        Roman_to_numeral = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D": 500, "M": 1000}
        placed_after = ("V","X","C","D","M","L")
        placed_before = ("I","X","C")
        Results = (4,9,40,90,400,900)     
       
        if len(s) == 1:
            return Roman_to_numeral[s[0]]
        
        num = Roman_to_numeral[s[0]]
        i = 1
        while i < len(s):
            if s[i - 1] in placed_before and s[i] in placed_after and (Roman_to_numeral[s[i]] - Roman_to_numeral[s[i - 1]]) in Results:
                
                num -= Roman_to_numeral[s[i - 1]]
                num  += (Roman_to_numeral[s[i]] - Roman_to_numeral[s[i - 1]])
                i += 1
            else:
                num += Roman_to_numeral[s[i]]
                i += 1
         
        return num
                
                
                