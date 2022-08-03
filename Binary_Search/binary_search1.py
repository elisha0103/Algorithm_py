import sys
input = sys.stdin.readline

n = int(input().rstrip())
parts = list(map(int, input().rstrip().split()))
m = int(input().rstrip())
req = list(map(int, input().rstrip().split()))

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] > target:
        return binary_search(array, target, start, mid-1)
    elif array[mid] == target:
        return mid
    else:
        return binary_search(array, target, mid+1, end)

parts.sort()

for i in req:
    result = binary_search(parts, i, 0, n-1)
    if result != None:
        print("yes", end=' ')
    else:
        print("no", end=' ')

        
