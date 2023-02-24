T = int(input())

for tc in range(T):
    string = input()

    stack = []

    ans = 1
    for i in range(len(string)):
        if string[i] == '{' or string[i] == '(':
            stack.append(string[i])

        if string[i] == '}' or string[i] == ')':
            if not stack:
                ans = 0
            elif string[i] == '}' and stack.pop() != '{':
                    ans = 0
            elif string[i] == ')' and stack.pop() != '(':
                    ans = 0

    if stack:
        ans = 0

    print(f'#{tc+1} {ans}')