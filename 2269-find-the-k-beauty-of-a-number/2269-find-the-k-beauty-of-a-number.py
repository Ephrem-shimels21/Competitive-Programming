class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = str(num)
        
        left = 0
        right = left + k - 1
        count = 0
        while right < len(num_str):
            sub_string = int(num_str[left : right + 1])
            
            if sub_string  and num % sub_string == 0:
                count += 1
            
            left += 1
            right += 1
            
        return count
                
            
        