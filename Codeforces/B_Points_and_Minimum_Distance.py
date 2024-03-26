def find_coord(arr):
    arr.sort()
    left = 0
    right = len(arr) - 1
    pairs = []
    while left < right:
        pairs.append((arr[left], arr[right]))
        left += 1
        right -= 1

    leng = 0
    for i in range(len(pairs) - 1):
        sx, sy = pairs[i]
        enx, eny = pairs[i + 1]
        leng += abs(enx - sx) + abs(eny - sy)

    return leng, pairs


test = int(input())

for _ in range(test):
    n = int(input())
    points = list(map(int, input().split()))
    min_leng, pairs = find_coord(points)
    print(min_leng)
    for pair in pairs:
        x, y = pair
        print(x, y)
