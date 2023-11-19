class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        left = 0
        right = 3
        s_dict = {}
        result = 0
        if len(s) < 3:
            return result
        for i in range(3):
            if s[i] not in s_dict:
                s_dict[s[i]] = 1
            else:
                s_dict[s[i]] += 1

           
        if len(s_dict) == 3:
            result += 1
            
        while right < len(s):
            if s[left] in s_dict:
                s_dict[s[left]] -= 1
                if s_dict[s[left]] == 0:
                    s_dict.pop(s[left])
                
            if s[right] not in s_dict:
                s_dict[s[right]] = 1
            else:
                s_dict[s[right]] += 1
            
            if len(s_dict) == 3:
                result += 1
                
            left += 1
            right += 1
            
        return result
                
            
        