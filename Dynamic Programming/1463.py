import sys
input = sys.stdin.readline

x = int(input())
d = [0] * (x+1)

for i in range(2, x+1):
    d[i] = d[i-1] + 1 # 현재의 수에서 1을 빼는경우, +1은 1을 뺀 계산 횟수를 추가한 것
    # 현재의 수에서 1을 빼는 경우, 3을 나눈 경우, 2를 나눈 경우 모두 비교해서 최솟값을 구할 것이다.
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] +1) # +1은 나누기 2를 한 계산 횟수를 추가한 것
        # d[i]의 +1은 위에서 했으므로 중복됨. 따라서 여기서는 안함
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] +1)
        
print(d[x])
