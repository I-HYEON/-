T = int(input())

for tc in range(T):
    N = int(input())
    matrix = [[i for i in input()] for _ in range(N)] # matrix 생성

    for i in range(N):  # matrix에서 2가 있는 좌표를 찾아 x,y에 저장
        for j in range(N):
            if matrix[i][j] == '2':
                x = i
                y = j

    # print('before while', (x,y))
    idx_x = [0,1,0,-1]
    idx_y = [1,0,-1,0]
    stack = [(x,y)]  # 현재좌표를 stack 에 담음
    ans = 0

    while stack:  # stack 에 좌표가 남아있으면 반복
        x, y = stack.pop()  # stack 에서 pop 해서 좌표를 x,y에 담기
        matrix[x][y] = '1'  # 해당 좌표는 이미 밟았으니까 1로 바꿈
        # print('first while',(x,y))
        for k in range(4):  # 4 방향 탐색
            nx = x + idx_x[k]
            ny = y + idx_y[k]
            if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] != '1':
                if matrix[nx][ny] == '3':
                    ans = 1
                    break
                elif matrix[nx][ny] == '0':
                    stack.append((nx, ny))

        if ans == 1:
            break
        x,y = nx, ny

    print(f'#{tc+1} {ans}')