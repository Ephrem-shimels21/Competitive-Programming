# Problem: Smallest Value After Replacing With Sum of Prime Factors - https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

class Solution:
    def smallestValue(self, n: int) -> int:

        while True:
            original, factors_sum, prime_factor = n, 0, 2

            while prime_factor <= n // prime_factor:
                while n % prime_factor == 0:
                    n //= prime_factor
                    factors_sum += prime_factor
                
                prime_factor += 1
            
            if n > 1:
                factors_sum += n
            
            if factors_sum == original:
                return original
            
            n = factors_sum
        