import sys
import heapq
input = sys.stdin.readline
INF = 987654321

# 총 마을, 간선 수, 시작 마을
n, m, start = map(int, input().rstrip().split())
# 마을 경로 입력 리스트
graph = [[] for _ in range(n+1)]
# 시작 마을부터 각 마을별로 갈 수 있는 최단거리 리스트
distance = [INF] * (n+1)

# 마을별 간선 입력
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b, c))

# 우선순위 큐로 다익스트라 구현
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

# 총 마을 수, 보낸 시간
city = 0
sendtime = 0

dijkstra(start)

# 시간은 못가는 마을 제외, 최단거리가 아닌 최대거리를 출력
for i in range(1, n+1):
    if distance[i] != INF:
        city += 1
        sendtime = max(sendtime, distance[i])

# 시작 마을 제외하기 때문에 -1을 한다
print(city-1, sendtime)
