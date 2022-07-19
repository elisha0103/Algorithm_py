import sys
num = int(sys.stdin.readline()  )
m = [0] * 10000

for i in range(num):
    a = int(sys.stdin.readline())
    m[a-1] += 1


for i in range(10000):               #인덱스 0~9999까지 탐색하는데 이는 1 ~ 10000을 의미, 이 숫자가 몇번 입력되었는지 확인하기 위해서 범위는 0~9999까지 탐색
    if m[i] != 0:
        for j in range(m[i]):
            print(i+1)

# * 계수 정렬(Counting Sort) 알고리즘
# - 배열의 인덱스를 특정한 데이터의 값으로 여기는 정렬 방법- 배열의 크기는 데이터의 범위를 포함할 수 있도록 설정
# - 데이터가 등장한 횟수를 셈
# - 유의사항 : 데이터의 개수가 많을 때 파이썬에서는 sys.stdin.readline()를 사용해야 함
# - sort 함수는 불필요한 메모리 소비를 하므로 초과됨
