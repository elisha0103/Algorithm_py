import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(computer, v, visited):
    visited[v] = True
    global cnt
    for i in computer[v]:
        if not visited[i]:
            cnt += 1 #다음 컴퓨터 감염 시켰으므로 +1 해준다.
            dfs(computer, i, visited)

n = int(input())
m = int(input())
computer = [[] for _ in range(n+1)]
visited = [False] * (n+1)
cnt = 0 #방문 횟수가 아닌 자신 외에 감염 시킨 컴퓨터를 세는 것이므로 0으로 시작

for i in range(m):
    x, y = map(int, input().split())
    computer[x].append(y)
    computer[y].append(x)

dfs(computer, 1, visited) #1번 컴퓨터부터 시작

print(cnt)
