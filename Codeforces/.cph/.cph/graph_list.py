from collections import defaultdict

nodes = int(input())
graph = defaultdict(list)

for i in range(nodes):
    node, neighbor, weight = map(int, input().split())
    graph[node].append((neighbor, weight))

print(graph)
