class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def is_nice(substr):
            return all((c.lower()  in substr and c.upper()  in substr) or (c.upper() in substr and c.lower() in substr) for c in substr)
        
        max_length = 0
        longest = ""
        n = len(s)
        for i in range(n):
            for j in range(i + 1, n + 1):
                subs = s[i : j]
                
                if is_nice(subs) and len(subs) > max_length:
                    longest = subs
                    max_length = len(subs)
                    
        return longest