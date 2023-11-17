class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums1)
        
        nums1_index = {}
        
        for i in range(len(nums1)):
            nums1_index[nums1[i]] = i
        
        stack = []
        
        for num in nums2:
            while stack and num > stack[-1]:
                cur = stack.pop()
                idx = nums1_index[cur]
                ans[idx] = num
            if num in nums1_index:
                stack.append(num)
        return ans
                            