class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        stack = deque()
        output = []
        for char in seq:
            if char == "(":
                if stack and stack[-1][1] == "(":
                    if stack[-1][0] == 0:
                        output.append(1)
                        stack.append((1,char))
                    elif stack[-1][0] == 1:
                        output.append(0)
                        stack.append((0,char))
                elif not stack:
                    output.append(0)
                    stack.append((0,char))
            
            elif char == ")":
                output.append(stack.pop()[0])
                
        return output
            