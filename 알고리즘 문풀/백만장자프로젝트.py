T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    money = 0

    while lst:  # 리스트안에 원소가 남아있으면 반복
        max_value = max(lst)
        max_idx = lst.index(max_value)

        if max_idx == 0: #  맥스 인덱스가 0이면 그냥 그걸 없애
            lst.pop(0)
        else: # 0이 아니면
            temp = 0
            # for i in range(max_idx):
            for i in range(max_idx-1, -1, -1):
                temp += max_value - lst.pop(i)

            money += temp

    print(tc, money)