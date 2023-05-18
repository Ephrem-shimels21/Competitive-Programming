class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        for num in  nums:
            if num not in freq.keys():
                freq[num] = 1
            elif num in freq.keys():
                freq[num] += 1
        
        for num in freq.keys():
            if freq[num] == 1:
                return num
            
        
        