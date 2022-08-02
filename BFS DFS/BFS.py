import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for i in range(n):
  graph.append(list(map(int, input().rstrip())))

  #이동할 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  #큐 구현을 위해 deque 라이브러리 사용
  queue = deque()
  queue.append((x, y))
#큐가 빌 때까지 반복
  while queue:
    x, y = queue.popleft()
    #현재 위치에서 네 방향의 위치 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        #맵을 벗어나면 무시
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
          continue
          #괴물이 있는 경우 무시
        if graph[nx][ny] == 0:
          continue
          #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
        if graph[nx][ny] == 1:
          graph[nx][ny] = graph[x][y] + 1
          #큐에 새로운 노드 입력, while문 반복
          queue.append((nx, ny))
          #가장 오른쪽 아래까지의 최단 거리 반환
  return graph[n-1][m-1]

print(bfs(0, 0))

#위 방법은 모든 인접 노드 방문을 하는데, 이 때 방문할때마다 0,0 지점에서 몇칸 떨어져있는지를 기록한다.
#그 후 모든 인접노드의 칸수가 기록이 되었으면 마지막 노드를 반환하여 출력하면 0,0 지점으로부터의 최단거리를 출력한다.
#마지막 지점에 갈 수 있는 경로가 여러가지의 경우의 수가 존재하지만 중복되지 않는 경우는 가장 짧은 최단거리로 큐에 먼저 삽입되기 때문
