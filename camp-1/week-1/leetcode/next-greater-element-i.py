class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums1)
        mon_stack = []

        for num in nums2:
            while mon_stack and num > mon_stack[-1]:
                poped = mon_stack.pop()
                if poped in nums1:
                    idx = nums1.index(poped)
                    ans[idx] = num
            mon_stack.append(num)
            
        return ans        