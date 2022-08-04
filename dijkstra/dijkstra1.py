import sys
input = sys.stdin.readline
INF = 987654321

n, m = map(int, input().split()) # 노드의 개수, 간선의 개수 입력
start = int(input()) # 시작 노드 번호 입력

graph = [[] for i in range(n+1)] # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
visited = [False] * (n+1) # 방문한 적이 있는지 체크하는 목적
distance = [INF] * (n+1)  # 최단 거리 테이블을 모두 무한으로 초기화

for _ in range(m): # 모든 간선 정보를 입력
    a, b, c = map(int, input().split()) # a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b, c))

def get_smallest_node(): # 방문하지 않은 노드 중에서 최단 거리 노드의 번호를 반환
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]: # 기존 최단거리보다 짧고, 방문한 적이 없다면
            min_value = distance[i]  # 최단거리 수정
            index = i # index에 최단거리 노드 저장
    return index  # 최단거리 노드 반환

def dijkstra(start):
    distance[start] = 0  # 시작 노드에 대하여 초기화
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]  # 시작노드에서 다른노드로 가는 경로의 최단거리 값을 초기에 저장

    for i in range(n-1):  # 총 n번 반복 중에서 처음 한개를 뺀 n-1번만 반복
        now = get_smallest_node()  # 방문하지 않은 노드 중에서 최단 거리 노드를 반환
        # 처음 시작노드에서 다른 노드로 가는 경로의 최단거리 값을 저장했기 때문에
        # now에 저장되는 값은 시작 노드와 연결된 다음 노드를 가리킴,
        # 그리고 이 것을 시작노드 한개를 제외한 n-1개 노드에 반복
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1] # 새로 측정된 비용은 지금까지 노드의 최단거리 값 + 지금 노드에서 다음 노드로 가는 비용
            if cost < distance[j[0]]:  # 새로 측정된 비용이 기존 다음노드의 최단거리 비용보다 적다면 새로이 최신화
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
