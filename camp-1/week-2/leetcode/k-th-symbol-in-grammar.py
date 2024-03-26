class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        curr = 0
        def findKth(left, right, n):
            nonlocal curr
            if n < 1:
                return 

            mid = (right + left) // 2

            if k <= mid:
                right = mid
                findKth(left, right, n - 1)
            else:
                left = mid
                curr = 1 - curr
                findKth(left, right, n - 1)
        
        findKth(0, 2 **(n - 1), n - 1)

        return curr
            