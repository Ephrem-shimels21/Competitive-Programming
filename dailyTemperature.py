class Solution:
    def dailyTemperatures(self, temperatures):
        n, top = len(temperatures), -1
        res, stack = [0] * n, [0] * n
        for i in range(n):
            while top >= 0 and temperatures[i] > temperatures[stack[top]]:
                idx = stack[top]
                res[idx] = i - idx
                top -= 1
            top += 1
            stack[top] = i
        return res