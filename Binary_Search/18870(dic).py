import sys
input = sys.stdin.readline

n = int(input().rstrip())
m = list(map(int, input().rstrip().split()))
h = list(set(m))
h.sort()

dic = {h[i] : i for i in range(len(h))}

for i in m:
    print(dic[i], end=' ')
