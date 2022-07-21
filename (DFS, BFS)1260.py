from collections import deque
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

n, m, r = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    x, y = map(int, input().rstrip().split())
    graph[x].append(y)
    graph[y].append(x)

for i in graph:
    i.sort()


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        a = queue.popleft()
        print(a, end=' ')
        for i in graph[a]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


dfs(graph, r, visited)
visited = [False] * (n + 1)
print()
bfs(graph, r, visited)
