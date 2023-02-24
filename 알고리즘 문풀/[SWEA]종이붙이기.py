T = int(input())

for tc in range(1,T+1):
    N = int(input())

    def paper(N):
        if (N // 10) // 2 == 0:
            return 1
        else:
            if (N // 10) % 2:
                return paper(N - 10) * 2 - 1
            else:
                return paper(N - 10) * 2 + 1

    print(f'#{tc} {paper(N)}')

