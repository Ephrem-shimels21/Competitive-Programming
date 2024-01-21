class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letter_count = {}
        
        left = 0
        result = 0
        
        for right in range(len(s)):
            letter_count[s[right]] = 1 + letter_count.get(s[right], 0)
            
            if (right - left + 1) - (max(letter_count.values())) > k:
                letter_count[s[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)
        return result 
                
            
            
        