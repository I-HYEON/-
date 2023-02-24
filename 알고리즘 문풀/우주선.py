T = int(input())
delta_i = [-1, -1, -1, 0, 0, 1, 1, 1]
delta_j = [-1, 0, 1, -1, 1, -1, 0, 1]

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for i in range(N)]
    total = 0

    for i in range(N):
        for j in range(M):

            if (i, j) == (0, 0) or (i, j) == (0, M) or (i, j) == (N, 0) or (i, j) == (N, M):
                pass

            cnt = 0
            for k in range(8):
                ni = i + delta_i[k]
                nj = j + delta_j[k]
                if 0 <= ni < N and 0 <= nj < M and matrix[ni][nj] < matrix[i][j]:
                    cnt += 1
                    if cnt >= 4:
                        total += 1
                        break

    print(f'#{tc} {total}')
