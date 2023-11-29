class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        if str(x) == (num[::-1]):
            return True
        return False
        
        
        