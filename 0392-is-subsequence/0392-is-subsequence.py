class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while i < len(t) and j < len(s):
            if s[j] == t[i]:
                i += 1
                j += 1
            else:
                i += 1
        if j >= len(s):
            return True
        elif i >= len(t):
            return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         ss = list(s)
#         tt = list(t)
#         new = []
#         if len(ss) >= 2:
#             i = 2
#         for letter in tt:
#             if letter in ss[:i]:
#                 new.append(letter)
#                 i += 1
                
#         if ss == new:
#             return True
#         return False
        

        