import sys
input = sys.stdin.readline

n = int(input().rstrip())
m = list(map(int, input().rstrip().split()))
h = list(set(m))
h.sort()

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

result = 0
for i in m:
    result = binary_search(h, i, 0, len(h))
    print(result, end=' ')
