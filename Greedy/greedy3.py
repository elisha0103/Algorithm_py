count = int(input())
money = list(map(int, input().split()))
money.sort()

result = 1

for i in money:
    if result < i:
        break
    result += i

print(result)

# 본 문제는 리스트를 오름차순으로 정렬한다.
# 목표 금액을 1부터 시작하여 작은 돈부터 하나씩 꺼내어 만들 수 있는지 확인한다.
# 만들 수 있으면 목표금액에 현재 금액을 더하여 다음 목표 금액을 설정해둔다.
# 목표금액보다 꺼낸 돈이 작거나 같으면 해당 목표 금액을 만들 수 있다는 것으로 간주한다.
# 목표 금액미만까지는 전에 꺼낸 돈들로 조합하여 만들 수 있다.
# 최신화된 목표금액은 지금 꺼낸 돈을 기반으로 설정된 목표금액이다.
# 지금 꺼낸 돈이 목표 금액보다 크다면, 목표 금액을 만들 수 없게 된다.
# 왜냐하면 지금까지 꺼낸 돈으로는 목표금액을 만들 수 없어서 다른 돈을 꺼낸 것인데, 
# 목표금액보다 큰 돈을 꺼내게 되면 조합을 해도 항상 목표금액보다 커지게 된다.

# 목표금액에 대한 아이디어
# 오름차순으로 정렬하면 하이면, 
