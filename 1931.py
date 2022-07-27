import sys
input = sys.stdin.readline
#끝나는 시간을 오름차순으로 정렬한다. 회의가 빨리 끝나는대로 많은 회의를 진행할 수 있기 때문
#좌표 정렬 문제 중 y좌표 오름차순으로 정렬했던 것을 이용
n = int(input().rstrip())
arr = []
for _ in range(n):
    x, y = map(int, input().rstrip().split())
    arr.append([y, x]) #끝나는 시간, 시작시간으로 추가한 후

arr.sort() #정렬하면 끝나는시간 오름차순 정렬이 됨
for i in range(n):
    arr[i][0], arr[i][1] = arr[i][1], arr[i][0] #스와프를 진행하면 배열은 [시작시간, 끝나는시간]으로 저장함
                                                # 하지만 배열 순서는 끝나는 시간 오름차순으로 저장된다.

tmp = arr[0][1]  #끝나는 시간 변수
result = 1
for i in range(1, n):
    if arr[i][0] >= tmp: #회의 시작 시간이 전 회의 끝나는 시간보다 같거나 크다면
        result += 1 #회의 추가
        tmp = arr[i][1] #회의가 추가되었다면 그 회의 끝나는 시간을 다시 tmp 변수에 저장

print(result)
