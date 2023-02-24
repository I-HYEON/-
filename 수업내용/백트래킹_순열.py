# ```'''
# 1,2,3 이라는 원소를 가진 리스트의 순열을 만들어보자
# '''
# def f(i,k):
#     if i == k:
#         print (p)
#     else:
#         for j in range(i, k):
#             p[i], p[j] = p[j], p[i]
#             f(i+1, k)
#             p[i], p[j] = p[j], p[i]
#
#
# p = [1,2,3]
# N = len(p)
# f(0,N) #첫번째 인덱스랑 길이 #안돼.....```

def f(i, k):
    if i == k:
        global mini
        global N
        total = 0
        for r, c in zip(range(N), p):
            total += matrix[r][c]
        mini = min(total, mini)

    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            f(i+1, k)
            p[i], p[j] = p[j], p[i]


T = int(input())
for t in range(1, T+1):
    N = int(input())
    matrix = [[int(i) for i in input().split()] for _ in range(N)]
    p = list(range(N))
    mini = 10*N
    f(0, N)
    print(f"#{t}", mini)