# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words_length = len(words)
        masks = [0] * words_length

        for idx, word in enumerate(words):
            for letter in word:
                masks[idx] |= 1 << (ord(letter) - ord("a"))
        

        max_product = 0
    
        for i in range(words_length):
            for j in range(words_length):
                if masks[i] & masks[j] == 0:
                    max_product = max(max_product, len(words[i]) * len(words[j]))
        
        return max_product

        