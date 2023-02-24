for tc in range(10):
    num = int(input())
    N,M = map(int, input().split())

    def exponent(N,M):
        if M == 1:
            return N
        return N*exponent(N,M-1)

    print(f'#{num} {exponent(N,M)}')