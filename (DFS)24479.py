import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9) #재귀함수 최대 횟수 조정

n, m, r = map(int, input().split())
count = 1 #몇번째 방문하는지
visited = [0] * (n+1) #노드와 인덱스를 같이하기 위하여 n+1 visited 인덱스는 방문 순서를 나타냄. 1번 인덱스는 1번 노드가 아닌 첫번째, 값은 노드를 나타냄
#1번인덱스 값 5번 => 첫번째 방문 노드는 5번 노드

def dfs(visited, graph, r):
    global count #main 함수 내 변수 사용
    visited[r] = count #n번째 방문 노드 기록
    for i in graph[r]:
        if visited[i] == 0:  #방문안했다면
            count += 1  #방문하기위하여 count +=1
            dfs(visited, graph, i)



graph = [[] for _ in range(n+1)]
for i in range(m):
    x, y = map(int, input().rstrip().split()) #간선 내용 입력
    graph[x].append(y)
    graph[y].append(x)

for i in range(n+1):  #간선 리스트 원소 정렬
    graph[i].sort()

dfs(visited, graph, r)

for i in range(1, n+1):  #방문 순서 출력
    print(visited[i])

#visited[i] 의 값은 i번째 방문 노드를 나타냄
#노드 번호에 해당하는 count 수는, (노드번호)번째 방문 노드는 count 값이다.
#즉 count번째 노드 방문 순서는 해당 count 값이 일치하는 노드번호이다.
