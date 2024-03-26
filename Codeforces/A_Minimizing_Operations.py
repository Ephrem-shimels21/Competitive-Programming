test = int(input())


def my_func(arr):
    opr = 0
    maxe = max(arr)
    return maxe - arr[0]


for _ in range(test):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    print(my_func(arr))
