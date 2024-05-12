# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        def generate_permutations(mask):
            permutation = []
            for idx in range(len(s)):
                if mask & (1 << idx):
                    permutation.append(s[idx].upper())
                else:
                    permutation.append(s[idx].lower())
            
            
            return "".join(permutation)
        
        n = len(s)
        total_permutations = 1 << n
        result = set()
        for mask in range(total_permutations):
            result.add(generate_permutations(mask))
        return result
                

        