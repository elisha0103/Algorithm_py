INF = 987654321
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

# 2차원 리스트(그래프 표현)을 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

#자기 자신에게 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A 에서 B로 가는 비용은 C라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            # 만약 k와 a, b가 같아져도 상관이 없음
            # 만약 k가 a와 같을 경우 => min((a,b), (a,k(a)) + (k(a), b)) => min((a,b), (a,a) + (a,b)) => min((a,b), 0 + (a,b))
            # 만약 k가 b와 같을 경우 => min((a,b), (a,k(b)) + (k(b), b)) => min((a,b), (a,b) + (b,b)) => min((a,b), (a,b) + 0)

# 수행 결과를 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INFINITY", end = ' ')
        else:
            print(graph[a][b], end = ' ')
    print()

