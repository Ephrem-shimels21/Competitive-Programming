class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []
        
        for i in range(max(len(s), len(t))):
            if i < len(s) and s[i] != "#":
                stack_s.append(s[i])
            
            elif i < len(s) and s[i] == "#" and stack_s:
                stack_s.pop()
            
            
            if i < len(t) and t[i] != "#":
                stack_t.append(t[i])
            elif i < len(t) and t[i] == "#" and stack_t:
                stack_t.pop()
        
        if stack_s == stack_t:
            return True
        return False
        