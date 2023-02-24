T = int(input())

for tc in range(1, T+1):
    STR = input()
    stack = []
    ans = 1

    for i in STR:
        if i in '({':
            stack.append(i)
        elif i == ')':
            try:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    ans = 0
                    break
            except:
                ans = 0
                break
        elif i == '}':
            try:
                if stack[-1] == '{':
                    stack.pop()
                else:
                    ans = 0
                    break
            except:
                ans = 0
                break
    if stack:
        ans = 0

    print(f'#{tc} {ans}')