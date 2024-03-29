import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
h = list(map(int, input().rstrip().split()))

result = 0

start = 0
end = max(h)

while(start <= end):
    total = 0
    mid = (start + end) // 2
    for i in h:
        if i > mid:
            total += i - mid

        if total < m:
            end = mid - 1
        else:
            result = mid
            start = mid + 1

print(result)
