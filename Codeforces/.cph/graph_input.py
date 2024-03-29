from collections import defaultdict

graph = defaultdict(list)
n = int(input())

for i in range(n):
    row = list(map(int, input().split()))

    for j in range(len(row)):
        graph[i].append((j, row[j]))

print(graph)
