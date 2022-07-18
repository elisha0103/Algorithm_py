n, m = map(int,input().split())
board = []
for i in range(n):
    board.append(list(input()))
data = []
box_w = 0
box_b = 0

for i in range(n-7):
    for j in range(m-7):
        box_w = 0  #w로 시작했을 때 칠해야 하는 칸 개수
        box_b = 0  #b로 시작했을 때 칠해야 하는 칸 개수
        for k in range(i, i+8):
            for l in range(j, j+8):

                if (k+l) % 2 == 0:
                    if board[k][l] != 'W': #만약 짝수 칸이 W어야 하는 경우, 근데 짝수 칸에 B가 있는 경우
                        box_w += 1 #box_w로 칠한 횟수 증가
                    else:         #만약 짝수 칸이 B어야 하는 경우, 근데 짝수 칸에 W가 있는 경우
                        box_b += 1
                else:
                    if board[k][l] != 'B': #만약 홀수 칸이 B어야 하는 경우, 근데 홀수 칸에 W가 있는 경우
                        box_w += 1  #box_w로 칠한 횟수 증가
                    else:           #만약 홀수 칸이 W어야 하는 경우, 근데 홀수 칸에 B가 있는 경우
                        box_b += 1
        data.append(box_w)   #b로 시작했는데 배열 틀려서 칠한 칸 개수
        data.append(box_b)   #w로 시작했는데 배열 틀려서 칠한 칸 개수



print(min(data))
