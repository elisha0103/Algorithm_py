n = int(input())
people = list(map(int, input().split()))
people.sort()
data = [people[0]]

for i in range(1, n):
    data.append(data[i-1] + people[i])
result = sum(data)
print(result)
