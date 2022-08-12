# 최소신장 트리를 이용한 크루스칼 알고리즘
# 최소한의 비용으로 모두를 연결할 때 사용
# 모든 노드를 포함시키면서 사이클이 존재하지 않은 부분 그래프를 구성
# 1. 간선 데이터를 비용에 따라 오름차순으로 정렬
# 2. 간선 하나씩 확인하면서 현재의 간선이 사이클을 발생시키는지 확인(노드 연결 전, 서로 최종 루트 노드가 같은경우 사이클 발생)
# 3. 사이클이 발생하지 않은 경우 최소 신장 트리에 포함시키고, 발생한 경우 포함시키지 않는다.

# 루트노드를 찾는 함수
def find_parent(parent, x):
  if parent[x] != x:
    # 루트노드가 아닌경우, 재귀적으로 루트노드를 찾는다
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

# 노드를 연결한 후 루트노드를 바꾼다.
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

n, m = map(int, input().split())
parent = [0] *(n+1)

road = []  # 모든 간선을 담을 리스트(서로소 집합 알고리즘에서는 간선정보 입력받은 즉시 노드와 노드 연결 여부를 수행하여 별도 간선 리스트가 없음)
result = 0  # 최종 비용을 담을 변수


# 노드 자기 자신을 루트노드로 설정
for i in range(1, n+1):
  parent[i] = i

# 간선 정보 입력
for _ in range(m):
  a, b, cost = map(int, input().rstrip().split())
  # 비용을 기준으로 정렬 함수 이용하기 때문에 순서 변경
  road.append((cost, a, b))

road.sort()


for i in road:
  cost, a, b = i
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost

print(result)
