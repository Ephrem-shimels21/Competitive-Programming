line = int(input())
count = 0

for _ in range(line):
    data = input()
    if "++" in data:
        count += 1
    elif "--" in data:
        count -= 1
print(count)
