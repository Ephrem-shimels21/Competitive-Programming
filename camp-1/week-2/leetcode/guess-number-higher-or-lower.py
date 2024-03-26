# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        mid = (low + high) // 2
        response = guess(mid)
        while True:
            if response == -1:
                high = mid
                mid  = (low + high) / 2
            elif response == 1:
                low = mid
                mid = (low + high) / 2
            else:
                return int(mid)

            response = guess(mid)

        