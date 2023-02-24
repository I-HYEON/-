T = int(input())

for tc in range(T):
    string = input()
    stack = []
    for i in range(len(string)):
        if not stack:
            stack.append(string[i])
        else:
            if stack[-1] == string[i]:
                stack.pop()
            else:
                stack.append(string[i])

    print(f'#{tc+1} {len(stack)}')