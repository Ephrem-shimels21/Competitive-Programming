class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        multiplier, value = 0, 0
        score = 0
        for p in s:
            if p == "(":
                stack.append(0)
            elif p == ")":
                multiplier = stack.pop()
                if multiplier == 0:
                    value = 1
                elif multiplier > 0:
                    value = multiplier * 2
                
                if stack:
                    stack[-1] = stack[-1] + value
                elif not stack:
                    score += value
        return score
        
        
             
        
        
        
        
        
        
        
        
        
        
        
        
#         def normal(s):
#             stack = []
#             score = 0          
#             for index,p in enumerate(s):
#                 if p == "(":
#                     if s[index:] and s[index:][0] == s[index:][1]:
#                         score += not_normal(s[index :]) 
#                         break
#                     stack.append(p)
#                 elif p == ")":
#                     if stack[-1] == "(":
#                         stack.pop()
#                         score += 1
#             return score
            
#         def not_normal(s):
#             stack = []
#             score = 0
#             for index,p in enumerate(s):
#                 if p == "(":
#                     if score > 0:
#                         score += normal(s[index:])
#                         break
#                     else:
#                         stack.append(p)
#                 elif p == ")":
#                     if score == 0:
#                         score += 1
#                     else:
#                         score *= 2
#             return score
        
            
        
#         if s[0] == s[1]:
#             return not_normal(s)
#         else:
#             return normal(s)
                    
            
        