n, q = list(map(int, input().split()))

arr = list(map(int, input().split()))
arr.sort()

for i in range(1, len(arr)):
    arr[i] = arr[i - 1] + arr[i]


for _ in range(q):
    x, y = map(int, input().split())

    if n - x == 0:
        print(arr[n - (x - y) - 1])
    else:
        res = arr[n - (x - y) - 1] - arr[n - x - 1]
        print(res)
