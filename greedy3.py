count = int(input())
money = list(map(int, input().split()))
money.sort()

result = 1

for i in money:
    if result < i:
        break
    result += i

print(result)
