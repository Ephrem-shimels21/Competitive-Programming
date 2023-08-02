class Solution(object):
    def splitString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        indexs = [x for x in range(1,len(s))]
        # print("Ephrem",indexs)
        def backTrack(index):
            if len(stack) == 0:
                stack.append(int(s[:index + 1]))
            previous = stack[-1]
            if index >= len(s) - 1:
                return 
            found_valid_substring = False
            # print(index,stack,previous)
            for i in range(index + 1,len(s)):
                if (previous - int(s[index + 1:i+1])) == 1:
                    found_valid_substring = True
                    if int(s[index + 1: i + 1]) == int(s[index + 1:]) == 0:
                        stack.append(int(s[index + 1:]))
                        backTrack(len(s))
                        return
                    else:
                        stack.append(int(s[index + 1:i+1]))
                        backTrack(i)
                        return
            
            if not found_valid_substring:
                while stack:
                    stack.pop()
                current = indexs.pop(0)
                backTrack(current)
             
        backTrack(0)
        if len(stack) == 1:
            return False
        elif len(stack) > 1:
            return True
                
                
                    

            
            
            
        