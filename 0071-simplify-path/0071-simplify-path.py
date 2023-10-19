class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        ans = ""
        pattern = r"[ /]"
        result = re.split(pattern,path)
        
       
        for char in result:
            if stack and  char == ".." and stack[-1] != "/" :
                stack.pop()
            elif len(char) != 0 and char != ".." and char != ".":
                stack.append(char)
        
        if not stack:
            return "/"
        while stack:
            current = stack.pop()
            ans = "/" + current + ans
            
        return  ans
        