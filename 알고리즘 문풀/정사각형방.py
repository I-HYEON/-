T = int(input())
di = [-1,0,1,0]
dj = [0,1,0,-1]

for tc in range(1,T+1):
    N = int(input())
    rooms = [list(map(int,input().split())) for _ in range(N)]

    move_max = 0
    room_number = 0
    for i in range(N):
        for j in range(N):
            flag = True
            x,y = i,j
            move = 0
            while 0 <= x < N and 0 <= y < N: # 좌표 인덱스 안에 들어있으면 반복

                for k in range(4):  # 해당 좌표의 4방향을 탐색해서 다음 위치를 정한다
                    nx = x + di[k]
                    ny = y + dj[k]
                    if 0 <= nx < N and 0 <= ny < N:  # 4 방향을 탐색하다가
                        if rooms[nx][ny] == rooms[x][y]+1:  #  정확히 1큰 수가 들어있는 방을 만나면
                            move += 1  #  move에 1을 카운트 해주고 좌표를 그 곳으로 옮긴다
                            x = nx
                            y = ny
                            break  # 4 방향 탐색을 그만둔다
                else:
                    flag = False
                    break

                if flag == False:
                    break

            if move_max < move:
                move_max = move
                room_number = rooms[i][j]
            elif move_max == move:
                if room_number > rooms[i][j]:
                    move_max = move
                    room_number = rooms[i][j]

    print(f'#{tc}',room_number,move_max+1)