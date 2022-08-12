# 위상 정렬 알고리즘은 방샹 크래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열한 것이다.
# 즉, 그래프상에서 선후 관계(방향성)가 있다면 모든 선후 관계를 지키는 전체 순서를 파악할 수 있다.
# 전체 순서를 파악할 때에는 사이클이 발생하지 않는다. 한 붓 그리기와 유사하다고 할 수 있다. - 사이클 판별 도구는 모든 원소를 방문하기 전에 큐가 비는 것이다.
# 1. 진입 차수(특정 노드로 방향성을 갖는 간선)가 0인 노드를 큐에 넣는다.
# 2. 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다. - 도착지 노드의 진입차수 -1 연산으로 표현한다.
# 3. 새롭게 진입차수가 0인 노드를 큐에 넣고 반복한다.

# 노드의 개수와 간선의 개수를 입력받기
from collections import deque
v, e = map(int, input().split())
# 모든 노드에 대한 진입 차수는 0으로 초기화
indegree = [0] * (v+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for _ in range(v+1)]

# 방향 그래프의 모든 간선 정보를 입력받기
for _ in range(e):
  a, b = map(int, input().split())
  graph[a].append(b) # 노드 a에서 b로 이동 가능
  # 진입 차수를 1 증가
  indegree[b] += 1
  
# 위상 정렬 함수
def topology_sort():
  result = [] # 알고리즘 수행 결과를 담을 리스트, 위상 정렬 순서대로 입력받을 리스트
  q = deque() # 큐 기능을 위한 deque 라이브러리 사용
  
  # 처음 시작할 때는 진입 차수가 0인 노드를 큐에 삽입
  for i in range(1, v+1):
    if indegree[i] == 0:
      q.append(i)
      
   # 큐가 빌 때까지 반복 (사이클 판별)
  while q :
    # 큐에서 원소 꺼내기
    now = q.popleft()
    result.append(now)
    # 해당 원소와 연결된 모든 노드들의 진입차수를 1 빼기
    for i in graph[now]:
      indegree[i] -= -1
      # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
      if indegree[i] == 0:
        q.append(i)
        
  # 위상 정렬을 수행한 결과 출력
  for i in result:
    print(i, end=' ')
        

topology_sort()
