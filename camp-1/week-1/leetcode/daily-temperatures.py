class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans  = [0] * len(temperatures)

        for idx,temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                target = stack.pop()
                ans[target] = idx - target
            stack.append(idx)

        return ans
                    