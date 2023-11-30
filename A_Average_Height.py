test = int(input())

for _ in range(test):
    n = int(input())
    evens = []
    odds = []
    students = list(map(int, input().split()))

    for stu in students:
        if stu % 2 == 0:
            evens.append(str(stu))
        else:
            odds.append(str(stu))

    print(*odds + evens)
