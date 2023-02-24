T = int(input())

for tc in range(T):
    N,M = map(int,input().split())
    matrix = [list(map(int,input().split()))for i in range(N)]
    total = 0

    for i in range(N):
        cnt = 0
        for j in range(M):
            if matrix[i][j] == 1:
                cnt+=1
            else:
                if cnt > total:
                    total = cnt
                    cnt = 0
        if cnt > total:
            total = cnt

    for j in range(M):
        cnt = 0
        for i in range(N):
            if matrix[i][j] == 1:
                cnt+=1
            else:
                if cnt > total:
                    total = cnt
                    cnt = 0
        if cnt > total:
            total = cnt

    print(f'#{tc+1} {total}')