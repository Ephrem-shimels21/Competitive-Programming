class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10 ** 9 + 7
        if not n % 2:
            even = odd =  n // 2
        else:
            even = n // 2 + 1
            odd = n // 2
        
        def countgood(base, exponent):
            if exponent <= 0:
                return 1
            
            result =  countgood(base, exponent // 2) % mod
            result = (result ** 2) % mod
            if exponent  % 2:
                result *= base
            return result
    
        
        return (countgood(5, even) * countgood(4, odd)) % mod
            


        