class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
            res = 0
            getsum = k * threshold          
            base = 0
            for i in range(k):
                base += arr[i]
            if base >= getsum:
                res += 1
            for i in range(k,len(arr)):
                base = base + arr[i] - arr[i-k]
                if base >= getsum:
                    res += 1
            return res