def bfs():
    '''
    1. 입력된 미로에서 출발점을 읽어오고, 출발점에서 모든 탐색을 해서 종료점이 나오면 1 아니면0 반환
    2. 일단 미로에서 읽어온 출발점 좌표를 큐에 넣고 시작한다.
    3. 큐가 남아있으면 while 반복문을 돈다.
    3-1. now에 큐의 첫인덱스를 뽑아 넣는다. 이 때 방문기록용으로 미로 현재 위치에 1을 넣는다.
    3-2. now를 델타검색해서 4방향 탐색을 해서
         인덱스를 벗어나지 않으면 원소를 읽어와
         3이면 1을 반환
         0이면 큐에 어펜드
    4. while문이 돌 때마다 큐는 무조건 팝하는데, 어펜드는 안하게 되므로 큐가 비게 되면 끝남.
       끝났다는 것은 종료 노드인 3을 못찾았다는 거니까 0을 반환
    '''
    for i in range(100):
        for j in range(100):
            if maze[i][j] == 2:
                x,y = i,j

    Q = [(x,y)]

    while Q:
        now = Q.pop(0)
        now_x = now[0]
        now_y = now[1]
        maze[now_x][now_y] = 1

        for i,j in zip(delta_i,delta_j):
            new_x = now_x + i
            new_y = now_y + j
            if 0 <= new_x < 100 and 0 <= new_y < 100:
                if maze[new_x][new_y] == 3:
                    return 1
                elif maze[new_x][new_y] == 0:
                    Q.append((new_x,new_y))
    return 0

for _ in range(10):
    tc = int(input())
    maze = [list(map(int,list(input()))) for _ in range(100)]
    delta_i = [-1,0,1,0]
    delta_j = [0,1,0,-1]

    ans = bfs()
    print(f'#{tc}',ans)