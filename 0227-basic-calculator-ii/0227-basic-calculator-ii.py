class Solution:
    def calculate(self, s: str) -> int:
        s_n = s.replace(" ", "")
        
        stack = []
        cur_num = 0
        op = "+"
        n = len(s_n)
        
        for i in range(n):
            curr_char = s_n[i]
            
            if curr_char.isdigit():
                cur_num = cur_num * 10 + int(curr_char)
            
            
            if not curr_char.isdigit() or i == n - 1:
                if op == "+":
                    stack.append(cur_num)
                elif op == "-":
                    stack.append(-cur_num)
                
                elif op == "*":
                    stack.append(stack.pop() * cur_num)
                
                elif op == "/":
                    stack.append (int(stack.pop() / cur_num))
                
                op = curr_char
                cur_num = 0
                
        result = 0
        
        while stack:
            result += stack.pop()
        
        return result
        
                
                
    
                
                
            
                
                
            
                
            