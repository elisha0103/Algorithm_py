n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 # 총 그룹의 수

count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data :   # 공포도를 낮은 것부터 하나씩 확인하며
  count += 1      # 현재 그룹에 해당 모험가를 포함시키기
  if count >= i:  # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면 그룹 결성
    result += 1   # 그룹 추가
    count = 0     # 그룹 추가되었으니 파티원은 초기화
   
print(result)

# 본 문제는 최대의 팀을 만드는 것이므로 오름차순 정렬
# 최소의 팀을 만드는 것은 내림차순 정렬을 한다.

import sys
input = sys.stdin.readline

n = int(input().rstrip())
high_level = 0
count = 0
result = 0

arr = list(map(int, input().split()))
arr.sort(reverse = True)
max_len = len(arr)

for i in range(n):
  if arr[i] > max_len:
    continue
    
  if arr[i] >= high_level:
    high_level = arr[i]

  count += 1
    
  if high_level == count:
    result += 1
    count = 0
    high_level = 0


print(result)
