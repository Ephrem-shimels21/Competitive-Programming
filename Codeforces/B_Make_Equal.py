test = int(input())


def my_fun(arr):
    total = sum(arr)
    if total % len(arr):
        return "NO"
    target = total // len(arr)
    to_diff = 0
    for num in arr:
        if num < target:
            requ = target - num
            if to_diff and to_diff >= requ:
                to_diff -= requ
            else:
                return "NO"
        elif num == target:
            continue

        else:
            to_diff += num - target

    if to_diff:
        return "NO"
    return "YES"


for _ in range(test):
    n = int(input())
    arr = list(map(int, input().split()))

    print(my_fun(arr))
