n = int(input())
count = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1


print(count)

# 시간, 분, 초를 str로 변환해서 list 형식으로 만들어준다. 이후 이 리스트 안에 '3' 문자가 있는지 확인을 함
# 만약 or 연산으로 따로 따로 비교를 하게 되면 13분, 23분 등 숫자 안에 3이 들어있다는 것을 구분하기 어려워진다.
