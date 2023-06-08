class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        required = 0
        value = 0
        
        for num in nums:
            if num in freq.keys():
                freq[num] += 1
            else:
                freq[num] = 0
                freq[num] += 1
        for key in freq.keys():
            if freq[key] > value:
                required = key
                value = freq[key]
        return required
        
        