import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

result = 0
team = 0


if n // 2 >= m :
  team = m
  n = n - (team * 2)
  k = n - k
  if k >= 0:
    result = team
  else:
    k = -k
    if k % 3 != 0:
      result = team - (k//3 + 1)
    else:
      result = team - (k//3)
else:
  team = n // 2
  m = m - team
  k = m - k
  if k >= 0:
    result = team
  else:
    k = -k
    if k % 3 != 0:
      result = team - (k//3 + 1)
    else:
      result = team - (k // 3)

print(result)




# 더 짧고, 직관적인 코드로 다시 풀어보기
