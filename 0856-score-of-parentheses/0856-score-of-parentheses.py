class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        mul, value = 0,0
        score = 0
        
        for p in s:
            if p == "(":
                stack.append(0)
            
            elif p == ")":
                mul = stack.pop()
                if mul == 0:
                    val = 1
                elif mul > 0:
                    val = mul * 2
                
                if not stack:
                    score += val
                elif stack:
                    stack[-1] = stack[-1] + val
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
                    
            
        