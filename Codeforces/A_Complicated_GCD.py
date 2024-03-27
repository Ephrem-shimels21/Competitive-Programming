mod = 10**100


def gcd(a, b):
    if b == 0:
        return a % mod
    return gcd(b, a % b) % mod


def find_common_gcd(a, b):
    if a == b:
        return a

    res = gcd(a, a + 1)

    for i in range(a + 2, b + 1):
        if res < i:
            break
        curr = gcd(res, i)
        res = curr

    return res


a, b = map(int, input().split())


print(find_common_gcd(a, b))
