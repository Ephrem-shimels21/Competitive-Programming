# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        badV = ""
        l = 1
        r = n
        mid = (l + r) // 2

        while l <= r:
            if not isBadVersion(mid):
                l = mid + 1
                mid = (l + r)// 2
            elif isBadVersion(mid):
                badV = mid
                r = mid - 1
                mid = (l + r) // 2
        return badV