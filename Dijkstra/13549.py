import sys
input = sys.stdin.readline
MAX = 100001
from collections import deque

visited = [False] * MAX
distance = [-1] * MAX

n,m = map(int, input().rstrip().split())
q = deque()
q.append(n)
visited[n] = True
distance[n] = 0

while q:
    now = q.popleft()
    if now == m:
        print(distance[now])
        break
    if now * 2 < MAX and visited[now*2] == False:
        q.appendleft(now * 2)
        visited[now*2] = True
        distance[now*2] = distance[now]
    if now + 1 < MAX and visited[now+1] == False:
        q.append(now+1)
        visited[now+1] = True
        distance[now+1] = distance[now] + 1
    if now - 1 >= 0 and visited[now-1] == False:
        q.append(now-1)
        visited[now-1] = True
        distance[now-1] = distance[now] + 1
