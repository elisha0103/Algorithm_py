import sys
input = sys.stdin.readline

arr = list(input().rstrip().split('-'))

result = 0
for i in range(len(arr)):
  if arr[i].find('+') != -1:  #요소에 +가 들어간 문자열이 있다면
    m = list(arr[i].split('+')) #+ 기준으로 나누어 m에 리스트 저장
    for j in m:
      if i == 0: #만약 첫번째 항이라면
        result += int(j) #첫번째 항은 무조건 result에 더해야한다.
      else:
        result -= int(j) #두번째 항 이상이라면 result에서 뺀다.
  else:
    if i == 0:  #요소에 +가 없고, 첫번째 항이라면
      result += int(arr[i]) #첫번째 항은 무조건 result에 더한다.
    else:
      result -= int(arr[i]) #요소에 +가 없고 두번째 항 이상이라면 result에서 뺀다.


print(result)
