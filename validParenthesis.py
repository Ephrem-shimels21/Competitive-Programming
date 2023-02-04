class Solution:
    def isValid(self, s: str) -> bool:
        lefts="({["
        rights=")}]"
        stack=[]
        for char in s:
            if (not stack or stack) and (char in lefts):
                stack.append(char)
            elif(not stack  and  (char in rights)):
                return False
            elif (stack  and (char in rights)):
                if (rights.index(char) == lefts.index(stack[-1])):
                    stack.pop()
                else:
                    return False
        return True if not stack else False
