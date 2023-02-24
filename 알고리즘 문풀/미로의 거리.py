def bfs():
    '''
    1. 미로를 순회해서 숫자 2인 좌표를 읽어온다.
    2. 그 좌표를 큐에 넣고, 그걸 이용해 방문표시를 하고, while 반복문을 시작한다.
    3. while 반복문에서는 큐에 있는 걸 꺼내와서, 델타검색을 한다.
    3-1. 델타검색 시, 방문한적 없고, 0이면 그 좌표를 큐에넣고, 동시에 방문표시(거리표시)도 해준다.
    3-2. 델타검색 시, 3이면 현 좌표까지의 방문표시 거리-1 를 반환한다.
    4. while 문이 한번 돌때마다, 큐에 있는 맨 앞의 좌표를 꺼내 탐색하는 것이고, 언젠가 탐색할 0이 없게되면
       큐에 추가되는 좌표가 없어 while문이 끝난다.
    5. while 문이 다 돌아서 끝난다면 3을 못만났다는 뜻이므로 0을 반환한다.
    '''
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                x,y = i,j

    Q = [(x,y)]
    visited[x][y] = 1

    while Q:
        now_x, now_y = Q.pop(0)

        for di,dj in zip(delta_i,delta_j):
            next_x = now_x + di
            next_y = now_y + dj
            if 0<=next_x<N and 0<=next_y<N:
                if visited[next_x][next_y] == 0 and maze[next_x][next_y] ==0:
                    Q.append((next_x,next_y))
                    visited[next_x][next_y] = visited[now_x][now_y] + 1
                elif maze[next_x][next_y] == 3:
                    return visited[now_x][now_y] - 1
    return 0

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    maze = [list(map(int,list(input())))for i in range(N)]
    visited = [[0 for i in range(N)]for i in range(N)]
    delta_i = [-1,0,1,0]
    delta_j = [0,1,0,-1]

    result = bfs()
    print(f'#{tc}',result)