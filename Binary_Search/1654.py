import sys
input = sys.stdin.readline

k, n = map(int, input().rstrip().split())
cen = []
for _ in range(k):
    cen.append(int(input()))

start = 1
end = max(cen)

result = 0
total = 0

while(start <= end):
    total = 0

    mid = (start + end) // 2

    for i in cen:
        total += i // mid
        if total >= n:
            break
    if total < n:
        end = mid - 1
    else:
        start = mid + 1

print(end)
# end는 렌선의 최대길이
# start는 렌선의 최소 길이
# mid는 원하는 개수의 렌선을 만들 수 있도록 절단하는 위치
# 따라서 end는 mid 위치에서 자르고 난 렌선의 최대길이를 반환해줄 수 있다.
