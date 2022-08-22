import sys
input = sys.stdin.readline


n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
result = 0
for i in range(n-1): # 마지막 n-1번째와 n번째의 비교를 위해서 a는 최대 n-1번째, 인덱스로는 n-2까지 공을 집을 수 있다.
    for j in range(i+1, n):
        if arr[i] == arr[j]:  # 같은 공은 잡을 수 없으므로 다음으로 넘어간다.
            continue
        else:
            result = result + n - (j+1) + 1  # 정렬되어있으므로 다른 무게의 공을 집은 경우, 전체에서 현재 번째를 빼고 +1을 해주면 남은 공의 개수도 계산된다.
            # 위 공식은 인덱스 값으로 계산되는 것이므로 마지막에 + 1을 해줘야 인덱스에 따른 n번째 공이 된다.
            break

print(result)
