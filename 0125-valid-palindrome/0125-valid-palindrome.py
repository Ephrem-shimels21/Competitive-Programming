class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(s)
        new = ''
        for i in s:
            if (ord(i) >= 65 and ord(i) < 91) or (ord(i) >= 97 and ord(i) < 123) or (ord(i) <= 57 and ord(i) >= 48):
                new += i
        new = new.lower()
        reversed_s = new[::-1]
        if new == reversed_s:
            return True
        return False
        