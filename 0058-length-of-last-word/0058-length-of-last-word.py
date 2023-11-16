class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        right = 0
        length = 0
        temp = 0
        while right < len(s):
            if ord(s[right]) != 32 :
                temp += 1
                if right == len(s) - 1:
                    length = temp
            elif temp and  ord(s[right]) == 32:
                length = temp
                temp = 0
           
            right += 1
        return length
                
            
            
            
            
        