import sys
input = sys.stdin.readline
import heapq
INF = 987654321

n, m = map(int, input().rstrip().split())
start = int(input())
distance = [INF] * (n+1)

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
