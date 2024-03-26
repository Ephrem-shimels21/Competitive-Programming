def find_divisors(a):
    final = 0

    for n in range(2, a + 1):
        i = 2
        res = []

        while i * i <= n:
            while n % i == 0:
                if i not in res:
                    res.append(i)
                n //= i
            i += 1

        if n > 1:
            res.append(n)

        if len(res) == 2:
            final += 1

    return final


n = int(input())

print(find_divisors(n))
