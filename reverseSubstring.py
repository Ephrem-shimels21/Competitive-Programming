class Solution:
        def reverseParentheses(self, s: str) -> str:
            stack = []
            for i in range(0, len(s)):            
                if s[i] != ')':
                    stack.append(s[i])
                else:
                    k = []
                    
                    while len(stack)!=0 and stack[-1]!='(':
                        k.append(stack.pop())
                    
                    stack.pop() 
                    k = k[::-1] 
                    while len(k)!=0:
                        stack.append(k.pop())
            return "".join(stack)