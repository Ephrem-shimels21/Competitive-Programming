class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        twn = 2 * len(nums)
        stack = []
        ans = [-1] * len(nums)

        for i in range(twn):
            if i >= len(nums):
                idx = (i + len(nums)) % twn
            else:
                idx = i
            
            while stack and nums[stack[-1]] < nums[idx]:
                target = stack.pop()
                ans[target] = nums[idx]
            stack.append(idx)

        return ans





       