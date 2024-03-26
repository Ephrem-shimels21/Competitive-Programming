class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_length = float("inf")
        substring = ''
        left = 0
        Have = 0
        needed = len(t)
        window = {}
        t_dict = {}
        for char in t:
            t_dict[char] = 1 + t_dict.get(char, 0)
        
        for right in range(len(s)):
            if s[right] in t_dict:
                window[s[right]] = 1 + window.get(s[right], 0)
                if window[s[right]] <= t_dict[s[right]]:
                    Have += 1
            else:
                continue
            
            if Have >= needed:
                if right - left + 1 < min_length:
                    substring = (left,right + 1)
                    min_length = right - left + 1
                while Have >= needed:
                    if s[left] in t_dict:
                        window[s[left]] -= 1
                        if window[s[left]] < t_dict[s[left]]:
                            Have -= 1
                    left += 1
                    if Have >= needed:
                        if right - left + 1 < min_length:
                            min_length = right - left + 1
                            substring = (left, right + 1)
                 

        if substring:
            return s[substring[0] : substring[1]]
        return substring
                    
                        
                        
            
            
            
        

        
        
        
        
        
        