for tc in range(10):

    number, string = input().split()

    N = int(number)
    stack = []
    for i in string:
        if not stack:
            stack.append(i)
        else:
            if stack[-1] != i:
                stack.append(i)
            else:
                stack.pop()

    print(f'#{tc+1}',''.join(stack))