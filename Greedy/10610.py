import sys
input = sys.stdin.readline

n = list(map(int, input().rstrip()))
if sum(n) % 3 != 0:
  print("-1")
else:
  n.sort(reverse=True)
  if n[-1] == 0:
    n_len = len(n)
    for i in range(n_len):
      print(n[i],end = '')
  else:
    print("-1")
    
    
# 배수 판별법에 대한 지식이 필요
