import sys
import copy
input = sys.stdin.readline
from collections import deque

n = int(input())

indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
time = [0] * (n+1)

for i in range(1, n+1):
    data = list(map(int, input().rstrip().split()))
    time[i] = data[0]
    for j in data[1:-1]:
        indegree[i] += 1
        graph[j].append(i) # 입력받는 내용이 i번째 노드가 data[j]로부터 출발하여 도착하여야 한다이므로
        # graph[j]는 j에서 출발해서 i로 도착한다. 가 되도록 코드 구성


def topology_sort():
    q = deque()
    result = copy.deepcopy(time) # 깊은 복사, 내용을 그대로 복사하고 메모리를 독립적으로 구성

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1 # 간선 하나 삭제 (절대 -= 연산 뒤에 -1로 하지 말것, -(-1) 연산이 되어버림)

            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n+1):
        print(result[i])

topology_sort()
