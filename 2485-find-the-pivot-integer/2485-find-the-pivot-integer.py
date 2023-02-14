class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1
        prefixSum = [0 for i in range(n+1)]
        for i in range(1,n+1):
            prefixSum[i] = prefixSum[i-1] + i
        prefixSum = prefixSum[1:]
        for j in range(1,len(prefixSum)):
            if prefixSum[j] == prefixSum[-1] - prefixSum[j-1]:
                return j + 1
        return -1