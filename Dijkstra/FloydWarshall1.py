import sys
input = sys.stdin.readline
INF = 987654321

n, m = map(int, input().rstrip().split())
graph = [[INF] * (n + 1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().rstrip().split())

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = graph[1][k] + graph[k][x]

if result >= INF:
    print("-1")
else:
    print(result)
