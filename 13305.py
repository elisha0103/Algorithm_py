n = int(input()) # 도시의 개수
distance = list(map(int, input().split())) # 도시 사이 길이
price = list(map(int, input().split())) # 도시의 주유 가격

result = price[0] * distance[0]
low_price = price[0]
total_distance = distance[0]

for i in range(1, n-1):
    if low_price <= price[i]:
        result += distance[i] * low_price
    else:
        low_price = price[i]
        result += distance[i] * low_price

print(result)
