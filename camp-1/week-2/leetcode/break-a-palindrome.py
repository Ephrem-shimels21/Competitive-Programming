class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        a_list = list(palindrome)
        left = 0
        if len(palindrome) == 1:
            return ""
        
        right = len(a_list) - 1

        while left < len(palindrome) and  a_list[left] == a_list[right] == "a":
            left += 1
            right -= 1

        
        if left == right:
            if left + 1 == len(palindrome) - 1:
                a_list[left + 1] = "b"
            else:
                a_list[len(palindrome) - 1] = "b"
    
        elif left == len(palindrome):
            a_list[left - 1] = "b"
        else:
            a_list[left] = "a"
        
        return "".join(a_list)
        
        
       