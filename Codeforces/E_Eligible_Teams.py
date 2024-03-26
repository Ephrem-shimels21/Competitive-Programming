test = int(input())

for _ in range(test):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    fast = n - 2
    slow = n - 1
    team = 0
    i = 2
    while fast >= 0:
        if arr[slow] >= x and arr[fast] >= x:
            team += 2
            fast -= 2
            slow -= 2
        elif arr[slow] >= x:
            team += 1
            slow = fast
            fast -= 1
        elif (arr[fast] * ((slow - fast) + 1)) >= x:
            size = (slow - fast) + 1
            team += 1
            slow -= size
            fast -= size
        else:
            fast -= 1

    print(team)
