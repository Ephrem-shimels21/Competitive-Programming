class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t = list(t)
        for char in s:
            if char not in t:
                return False
            else:
                t.remove(char)
        if len(t) == 0:
            return True 
            
        