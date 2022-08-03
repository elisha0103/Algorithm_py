n, m = map(int, input().split())         # 맵 세로, 가로 길이
pos_h, pos_w, arrow = map(int, input().split())   # 현재 캐릭터 위치, 바라보는 방향
arr = []    # 맵 크기 설정 (이중리스트)
for _ in range(n):
     arr.append(list(map(int, input().split())))  # 맵 크기를 2중 리스트로 입력받음, 한줄에 4개의 길이가 있는 리스트

count = 1  # 방문 위치 개수
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]   # 캐릭터가 한 방향으로 이동할 때 해당 방향에 대한 위치변화량 (북, 동, 남, 서) = (위, 좌, 하, 우)
arrow_count = 0 # 캐릭터의 방향전환량 체크 변수 => 4번 방향전환을 하면 더이상 갈 곳이 없다고 판단
while True:
    if arrow <0:  #왼쪽으로 돌 때마다 move 리스트의 인덱스는 -1씩 감소함
                  #왼쪽으로 돌 때마다 arrow를 -1씩 해주어 arrow를 move의 인덱스로 사용할 텐데,
        arrow +=4 # move[-1]는 move[3] 이므로, 추후 index 오류 방지를 위해 arrow 값이 음수가 되면 +4를 해줌
    next_move = [move[arrow][0] + pos_h, move[arrow][1] + pos_w]  #next_move = [다음 h값, 다음 w값]
    if next_move[0] < 0 or next_move[1] < 0: #맵 서쪽, 북족을 벗어나게 되면 방향을 바꾼다.
        arrow -= 1
        arrow_count += 1
    elif next_move[0] >=n or next_move[1] >= m: #남쪽, 동쪽을 벗어나게 되면 방향을 바꾼다.
        arrow -= 1
        arrow_count += 1

    if arr[next_move[0]][next_move[1]] != 1 :    # 갈 수 있으면 가고 안되면 왼쪽으로 방향을 튼다.
        arr[pos_h][pos_w] = 1  # 갈 수 있다면 가기 전 현재 위치를 방문표시로 바꿔준다. 
                               # 방문한 장소랑 바다는 어쩌피 못가므로 1로 값을 표시한다.
        pos_h, pos_w = next_move[0], next_move[1]  
        count += 1
        arrow_count = 0  #캐릭터가 이동했으므로 방향전환 체크변수의 값은 다시 0으로 초기화한다.
    else:
        arrow -= 1
        arrow_count+=1

    if arrow_count == 4:
        break
    print(pos_h, pos_w, arrow)  #캐릭터의 현재 움직임

print(count)

