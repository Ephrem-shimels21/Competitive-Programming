class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""
        
        uniques = set(s)
        
        for idx, character in enumerate(s):
            if character.swapcase() not in uniques:
                left = self.longestNiceSubstring(s[:idx])
                right = self.longestNiceSubstring(s[idx + 1:])
            
                return left if len(left) >= len(right) else right
        
        return s