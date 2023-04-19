class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magaz = []
        magaz[:0] = magazine
    
        for letters in ransomNote:
            if letters not in magaz:
                return False
            elif letters in magaz:
                magaz.remove(letters)
        return True 
        