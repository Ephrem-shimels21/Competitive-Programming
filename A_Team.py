n = int(input())
n_p = 0
for _ in range(n):
    view = sum(list(map(int, input().split())))
    if view >= 2:
        n_p += 1

print(n_p)
