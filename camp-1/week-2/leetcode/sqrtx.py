class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        mid = (low + high) // 2
        result = 0
        while low <= high:
            if mid ** 2 > x:
                high = mid - 1
                mid = (low + high) // 2
            elif mid ** 2 < x:
                result = mid
                low = mid + 1
                mid = (low + high) // 2
            else:
                return mid
        return result

           