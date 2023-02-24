for tc in range(10):
    N = int(input())
    tmp = list(input())

    rlt = []
    stack = []

    for i in tmp:

        if i in '+':
            stack.append(i)
        else:
            rlt.append(i)

    while stack:
        rlt.append(stack.pop())

    result = ''.join(rlt)
    # print(result)

    stack = []  # 빈 스택 생성
    for i in result:  # 후위표기법 문자열을 하나씩 순회
        if len(stack) >= 2:  # 스택에 이미 두개 이상 있으면
            if i == '+':  # '+'이면 스택의 두 개를 더해서 스택에 추가
                stack.append(stack.pop()+stack.pop())
            else:
                stack.append(int(i))
        else:
            stack.append(int(i))

    print(f'#{tc+1}',*stack)