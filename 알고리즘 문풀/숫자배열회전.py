T = int(input())

for tc in range(1,T+1):
    N = int(input())

    num_board = []
    for i in range(N):
        num_board.append(list(map(int,input().split())))
    # 입력값 이차원배열을 받아옴

    def turn_90(matrix):
        new_matrix = [[0 for j in range(len(matrix))]for i in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                new_matrix[j][len(matrix)-i-1] = matrix[i][j]

        return new_matrix

    matrix_90 = turn_90(num_board) #90도 회전한 배열
    matrix_180 = turn_90(matrix_90) #180도 회전한 배열
    matrix_270 = turn_90(matrix_180) #270도 회전한 배열

    # print(matrix_90)
    # print(matrix_180)
    # print(matrix_270)
    print(f'#{tc}')
    for a,b,c in zip(matrix_90,matrix_180,matrix_270):
        for i in a:
            print(i,end="")
        print(" ",end="")
        for i in b:
            print(i,end="")
        print(" ", end="")
        for i in c:
            print(i,end="")
        print()