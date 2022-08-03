import sys
input = sys.stdin.readline

n = int(input())
m = []
for i in range(n):
    m.append(list(map(int, input().rstrip().split())))

for i in range(1, n):
    m[i][0] = min(m[i-1][1], m[i-1][2]) + m[i][0]
    m[i][1] = min(m[i-1][0], m[i-1][2]) + m[i][1]
    m[i][2] = min(m[i-1][0], m[i-1][1]) + m[i][2]

print(min(m[n-1]))

# m 리스트에 n번째 집에 빨간색, 초록색, 파랑색을 색칠할 경우, 각 색의 총 비용을 계산하여 대체한다.
# 예) 1번 집에 빨간색을 할 경우 최솟값 => 0번째 집에 파랑, 초록을 칠한 경우의 최솟값 + 1번집에 빨간색 칠하는 비용
# 예) 1번 집에 파란색을 할 경우 최솟값 => 0번째 집에 빨강, 초록을 칠한 경우의 최솟값 + 1번집에 파랑색을 칠하는 비용
# 이렇게 계속 진행하다가 n-1번째 집(실제 n번째 집)의 요소는 n번째 집이 색을 칠할 때 드는 비용 대신에 그동안의 총 합 최솟값으로 바뀌어져있다.
# 따라서 n-1번째 모든 요소의 최솟값을 구하면 원하는 답을 구할 수 있다.