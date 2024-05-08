# Problem: Number of Wonderful Substrings - https://leetcode.com/problems/number-of-wonderful-substrings/

class Solution:
    def wonderfulSubstrings(self, word):
        count_dict = {0: 1}  
        mask = 0 
        wonderful_count = 0  
        
        for char in word:
            mask ^= (1 << (ord(char) - ord('a')))
            
            if mask in count_dict:
                wonderful_count += count_dict[mask]
            
            for i in range(10):
                toggled_mask = mask ^ (1 << i)
                if toggled_mask in count_dict:
                    wonderful_count += count_dict[toggled_mask]
            
            if mask not in count_dict:
                count_dict[mask] = 1
            else:
                count_dict[mask] += 1
        
        return wonderful_count
