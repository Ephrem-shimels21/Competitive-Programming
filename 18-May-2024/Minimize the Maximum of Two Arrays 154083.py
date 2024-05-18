# Problem: Minimize the Maximum of Two Arrays - https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/

class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        def lcm(a, b):
            return a * b // gcd(a, b)

        def condition(x: int) -> bool:
            nondiv_cnt1 = x - (x // divisor1)
            nondiv_cnt2 = x - (x // divisor2)
            lcm_value = lcm(divisor1, divisor2)
            nondiv_cnt_total = x - (x // lcm_value)
            return (
                nondiv_cnt1 >= uniqueCnt1 and
                nondiv_cnt2 >= uniqueCnt2 and
                nondiv_cnt_total >= uniqueCnt1 + uniqueCnt2
            )

        low, high = 1, 10**10
        while low < high:
            mid = (low + high) // 2
            if condition(mid):
                high = mid
            else:
                low = mid + 1

        return low
