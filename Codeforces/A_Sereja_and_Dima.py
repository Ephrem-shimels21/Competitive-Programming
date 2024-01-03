n = int(input())

arr = list(map(int, input().split()))

ps = True
s_sum = 0
d_sum = 0

l, r = 0, n - 1

while l <= r:
    if arr[l] > arr[r]:
        if ps:
            ps = False
            s_sum += arr[l]
            l += 1
        else:
            d_sum += arr[l]
            l += 1
            ps = True
    else:
        if ps:
            ps = False
            s_sum += arr[r]
            r -= 1
        else:
            d_sum += arr[r]
            r -= 1
            ps = True

print(s_sum, d_sum)
