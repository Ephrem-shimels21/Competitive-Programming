class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        mod = 10 ** 9 + 7
        next_sm = [n] * n
        prev_sm = [-1] * n
        stack = []
        stackp = []

        for idx, num in enumerate(arr):
            while stack and arr[stack[-1]] >= num:
                target = stack.pop()
                next_sm[target] = idx
            
            stack.append(idx)
        
        for idx, num in enumerate(arr):
            while stackp and arr[stackp[-1]] >= num:
                stackp.pop()
            if stackp and  arr[stackp[-1]] < num:
                target = stackp[-1]
                prev_sm[idx] = target
            elif stackp and arr[stackp[-1]] > num:
                stackp.pop()
            stackp.append(idx)
        
        ans = 0
        for i in range(n):
            left = i - prev_sm[i]
            right = next_sm[i] - i
            subarr = left * right
            ans += arr[i] * subarr

        return ans % mod
            





        