def pascar(num_list, M):
    if M == 0:
        return num_list
    else:
        new = []
        for i in range(len(num_list)):
            if i == 0:
                new.append(num_list[i])
            else:
                new.append(num_list[i - 1] + num_list[i])
        new.append(1)
    return pascar(new, M - 1)

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}')
    for j in range(N):
        print(*pascar([1],j))