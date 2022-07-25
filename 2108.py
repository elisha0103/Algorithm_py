import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
arr = []
for _ in range(n):
  arr.append(int(input().rstrip()))

arr.sort()
print(round(sum(arr)/n)) #산술평균
print(arr[n//2]) # 중앙값

cnt = Counter(arr).most_common()
#print(cnt)
#[(-2, 1), (1, 1), (2, 1), (3, 1), (8, 1)]
#(value, 빈도수) 튜플 형식으로 반환

if len(cnt) > 1: #만약 빈도수 튜플이 1개 이상일경우,
  if cnt[0][1] == cnt[1][1]: #최빈도수가 같은경우,
    print(cnt[1][0]) #두번째로 작은값을 출력
  else: print(cnt[0][0]) #최빈도수가 다른경우, 최빈값 출력
else:print(cnt[0][0]) #만약 빈도수 튜플이 1개만 있을경우 최빈값은 1개

print(max(arr)-min(arr))
