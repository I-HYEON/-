for _ in range(10):
    tc = int(input())

    matrix = []  # 2차원배열을 matrix에 담음
    for i in range(100):
        matrix.append(list(input()))

    max_palin = 0  # 가장긴회문길이를 0으로 초기화

    # 가로순회
    for i in range(100):
        for j in range(100):  # 모든 좌표에 접근해서 가능한 회문 모두 검토

            for k in range(100 - j, 0, -1):  # 길이를 거꾸로 접근
                # 근데 (99-j,-1,-1)이라고 생각했는데 답이 오차존재.
                # (100-j,0,-1)이나 (100-j,-1,-1) 둘다 정답나옴. 왜???
                # k의 인덱스가 필요한게 아니라 k만큼의 범위가 필요하기 때문에 그럼!
                # 지금 인덱스가 맞음~~~
                STR = ''
                for l in range(k):
                    STR += matrix[i][j + l]

                if STR == STR[::-1] and max_palin <= len(STR):
                    max_palin = len(STR)
                    break
    # 세로순회
    for j in range(100):
        for i in range(100):

            for k in range(100 - i, 0, -1):
                STR = ''
                for l in range(k):
                    STR += matrix[i + l][j]

                if STR == STR[::-1] and max_palin <= len(STR):
                    max_palin = len(STR)
                    break

    print(f'#{tc} {max_palin}')