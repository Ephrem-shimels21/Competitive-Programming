n, k = list(map(int, input().split()))

arr = list(map(int, input().split()))

count = 0

num_k = arr[k - 1]

for i in range(n):
    if arr[i] >= num_k and arr[i] > 0:
        count += 1
    elif arr[i] < num_k:
        break
print(count)
