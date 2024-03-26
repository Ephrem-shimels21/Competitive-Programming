class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        print(path)

        for dirc in path:
            if dirc == "..":
                if stack:
                    stack.pop()
            elif dirc != "."  and  dirc != "":
                stack.append(dirc)
          
           
        return  "/" + "/".join(stack)

                
        