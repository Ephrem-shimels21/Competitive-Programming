from collections import Counter

n, m = list(map(int, input().split()))


arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1_c = Counter(arr1)
arr2_c = Counter(arr2)


count = 0

for num in arr1_c:
    if num in arr2_c:
        count += arr1_c[num] * arr2_c[num]

print(count)
