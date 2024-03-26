class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openings = "([{"
        closings = ")]}"

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


        