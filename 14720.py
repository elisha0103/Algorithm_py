n = int(input())
m = list(map(int, input().split()))
result = 0
count = 0
for i in range(n):
    if m[i] == count:
        count +=1
        result += 1
    if count >= 3:
        count = 0


print(result)
