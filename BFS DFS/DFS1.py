import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().rstrip())))

def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True #graph[x][y]가 상하좌우 탐색을 하면서 아이스크림 구역이 존재한다면 True 반환하여 개수 1을 증가시키기 위함
    return False  #graph[x][y]가 1이라면 false 반환


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
print(result)
