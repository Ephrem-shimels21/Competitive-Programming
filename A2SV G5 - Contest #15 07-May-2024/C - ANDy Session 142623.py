# Problem: C - ANDy Session - https://codeforces.com/gym/522079/problem/C

tests = int(input())


def find_max_result(arr, k):
    length = len(arr)
    result = 0

    for pos in range(30, -1, -1):
        count = sum(1 for num in arr if num & (1 << pos))
        operations_needed = length - count

        if k >= operations_needed:
            result |= 1 << pos
            k -= operations_needed

    return result


for _ in range(tests):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    print(find_max_result(arr, k))
