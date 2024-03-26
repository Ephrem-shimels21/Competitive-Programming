from collections import defaultdict

test = int(input())


for _ in range(test):
    leng = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a_count = defaultdict(int)
    b_count = defaultdict(int)
    a_count[a[0]] = 1
    b_count[b[0]] = 1
    countA = 1
    countB = 1
    for i in range(1, leng):
        if a[i] == a[i - 1]:
            countA += 1
        else:
            if a_count[a[i - 1]] < countA or a[i - 1] not in a_count:
                a_count[a[i - 1]] = countA

            countA = 1
        if b[i] == b[i - 1]:
            countB += 1
        else:
            if b_count[b[i - 1]] < countB or b[i - 1] not in b_count:
                b_count[b[i - 1]] = countB
            countB = 1

    if countA > a_count[a[-1]] or a[-1] not in a_count:
        a_count[a[-1]] = countA
    if countB > b_count[b[-1]] or b[-1] not in b_count:
        b_count[b[-1]] = countB

    max_leng = 0

    c = a + b
    c_unique = list(set(c))

    for num in c_unique:
        res = a_count[num] + b_count[num]
        max_leng = max(max_leng, res)

    print(max_leng)
