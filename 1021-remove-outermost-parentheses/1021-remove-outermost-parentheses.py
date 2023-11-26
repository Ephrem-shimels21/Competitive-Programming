class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        stack = []
        
        for pare in s:
            if pare == "(":
                if stack:
                    result += "("
                stack.append(pare)
            
            elif stack and pare == ")":
                left = stack.pop()
                if stack:
                    result += pare
                    
        return result
                   
        