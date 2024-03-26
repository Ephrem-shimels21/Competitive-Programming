class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffixPr = [nums[len(nums) - 1]]
        prefixPr = [nums[0]]

        for i in range(1, len(nums)):
            prefixPr.append(prefixPr[i - 1] * nums[i])
        
        for i in range(len(nums) - 2, -1, -1):
            suffixPr = [suffixPr[0] * nums[i]] + suffixPr
            
        prefixPr = [1] + prefixPr
        suffixPr = suffixPr + [1]
        
        ans = []

        for i in range(1,len(nums) + 1):
            ans.append(prefixPr[i - 1] * suffixPr[i])
        
        return ans

        