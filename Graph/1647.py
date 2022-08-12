import sys
input = sys.stdin.readline

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

road = []
result = 0
# 최소신장 트리를 완성한 후(한 개의 마을), 두개의 마을로 분할하기 위해서는
# 가장 비싼 길 하나를 제거하면 최소 비용으로 두개의 마을이 된다.
high_cost = 0

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
    # 최소신장 트리 구성 중 가장 비싼 간선을 확인한다
    if high_cost < cost:
      high_cost = cost

print(result - high_cost)
