class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def isValid(s: str) -> bool:
            stack = []
            openings = "("
            closings = ")"

            for par in s:
                if par in openings:
                    stack.append(par)
                elif par in closings:
                    if not stack:
                        return False
                    idx = openings.index(stack[-1])
                    if closings.index(par) == idx:
                        stack.pop()
                    else:
                        return False
            
            if stack:
                return False
            return True
        

        
        def generate(path, openings, closings):
            if closings > openings:
                return 
            if len(path) == 2 * n:
                if isValid("".join(path[:])):
                    res.append("".join(path[:]))
                return 
            path.append("(")
            generate(path, openings + 1, closings)
            path.pop()
            path.append(")")
            generate(path, openings , closings + 1)
            path.pop()
    
        res = []
        generate([], 0, 0)

        return res
            

        