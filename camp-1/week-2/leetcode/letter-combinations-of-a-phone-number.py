class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        number_letter = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        res = []

        def findComb(start, path):
            if not digits:
                return 
            if len(path) == len(digits):
                res.append("".join(path[:]))
                return 
                
            strr = number_letter[int(digits[start])]
            
            for i in range(len(strr)):
                path.append(strr[i])
                findComb(start + 1, path)
                path.pop()
        

        findComb(0,[])
        return res
        