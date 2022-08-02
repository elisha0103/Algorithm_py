# bfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
#     for each v ∈ V - {R}
#         visited[v] <- NO;
#     visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
#     enqueue(Q, R);  # 큐 맨 뒤에 시작 정점 R을 추가한다.
#     while (Q ≠ ∅) {
#         u <- dequeue(Q);  # 큐 맨 앞쪽의 요소를 삭제한다.
#         for each v ∈ E(u)  # E(u) : 정점 u의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다)
#             if (visited[v] = NO) then {
#                 visited[v] <- YES;  # 정점 v를 방문 했다고 표시한다.
#                 enqueue(Q, v);  # 큐 맨 뒤에 정점 v를 추가한다.
#             }
#     }
# }

from collections import deque
import sys
input = sys.stdin.readline  

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
cnt = 1
for _ in range(m):
  x, y = map(int, input().rstrip().split())
  graph[x].append(y)
  graph[y].append(x)

for i in graph:
  i.sort(reverse=True)
  
visited = [0] * (n+1)

def bfs(graph, start, visited):
  global cnt
  queue = deque([start])
  visited[start] = cnt

  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if visited[i] == 0:
        queue.append(i)
        cnt +=1
        visited[i] = cnt

bfs(graph, r, visited)
for i in range(1, n+1):
  print(visited[i])
