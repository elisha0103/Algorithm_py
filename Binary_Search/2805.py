import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
tree = list(map(int,input().rstrip().split()))

start = 0
end = max(tree) # 나무 길이 중 최댓값
result = 0

while(start <= end): # 파라메트릭 서치문제 유형은 반복문으로 구성
    total = 0
    mid = (start + end) // 2
    for x in tree:  # 트리 높이를 꺼내와서
        if x > mid:  # 중간값 보다 높으면
            total += x - mid  # total에 나무 - 중간값을 저장한다.
        if total > m:  # 이 때 이미 total 값이 m을 넘어섰으면 나머지 나무는 확인할 필요가 없으므로 탈출문 작성(시간초과를 막아줌)
            break
    if total < m:  # 만약 자른 나무가 목표치보다 낮다면 더 많이 잘라야하므로 mid는 앞으로 댕겨야한다.
        end = mid - 1
    else:  # 만약 자른 나무가 목표치보다 크다면 일단 result에 H값을 저장하고, mid를 뒤로 밀어놔서 더 좋은 값이 있는지 확인한다.
        result = mid
        start = mid + 1

print(result)
