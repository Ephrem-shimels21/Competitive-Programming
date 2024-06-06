# Problem: Reverse Substrings Between Each Pair of Parentheses - https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for char in s:
            if char != ")":
                stack.append(char)
            else:
                temp = []
                while stack and stack[-1] != "(":
                    temp.append(stack.pop())
                stack.pop()
                
                for curr in temp:
                    stack.append(curr)
        
        return "".join(stack)

        