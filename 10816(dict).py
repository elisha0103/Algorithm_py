import sys
input = sys.stdin.readline

n = int(input().rstrip())
a = list(map(int, input().rstrip().split()))
m = int(input().rstrip())
h = list(map(int, input().rstrip().split()))

def binary_search(array, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if array[mid] == target:
        return cnt.get(target)
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)
cnt = {}
a.sort()
for i in a:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in h:
    print(binary_search(a, i, 0, n-1), end=' ')
