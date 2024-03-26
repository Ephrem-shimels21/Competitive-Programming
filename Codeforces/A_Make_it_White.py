test = int(input())

for _ in range(test):
    leng = int(input())
    cells = input()
    left = 0
    right = leng - 1

    while left <= right:
        if cells[left] == "W":
            left += 1

        if cells[right] == "W":
            right -= 1

        if cells[left] == cells[right] == "B":
            print(right - left + 1)
            break
