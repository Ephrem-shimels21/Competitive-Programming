# Problem: Replace Elements with Greatest Element on Right Side - https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_sof = -1
        ans = [0] * len(arr)
        
        for i in range(len(arr) - 1, -1, -1):
            ans[i] = max_sof
            max_sof = max(max_sof, arr[i])
        
        return ans

        