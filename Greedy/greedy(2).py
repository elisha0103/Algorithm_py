n , m , k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[-1]
second = data[-2]

count = (m//(k+1))*k + (m%(k+1))

result = 0
result = count * first + (m-count) * second
print(result)

# 단순 반복말고 반복하여 더했을 때, 나타나는 규칙을 통해서 계산
