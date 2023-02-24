T = int(input())

for tc in range(1,T+1):
    lst = list(input().split())  # 후위표기법 문자열을 리스트로 받아옴
    print(f'#{tc}',end=" ")

    stack = []  # 빈 스택 생성
    for i in lst:  # 후위표기법 문자열을 하나씩 순회
        if len(stack) >= 2:  # 스택에 이미 두개 이상 있으면
            if i == '+':  # '+'이면 스택의 두 개를 더해서 스택에 추가
                stack.append(stack.pop()+stack.pop())
            elif i == '-':  # '-'이면 스택의 두개를 빼서 스택에 추가
                stack.append(-stack.pop() + stack.pop())
            elif i == '*':  # '*'이면 스택의 두개를 곱해서 스택에 추가
                stack.append(stack.pop() * stack.pop())
            elif i == '/':  # '/'이면 스택의 두개를 나눠서 스택에 추가
                temp = stack.pop()
                stack.append(stack.pop()//temp)
            else:  # 연산자가 아니면
                if i == '.':  # '.'일경우 stack 에 두개 이상인데 .을 만났으므로 잘못된 것
                    print('error')
                else:  # 어느 하나에도 해당되지 않았으면 숫자이니까 stack에 append
                    stack.append(int(i))
        else:  # 스택길이가 0이나 1이면
            if i in '+-*/':  # 연산자를 만나면 error 발생
                print('error')
                break
            else:  # 연산자가 아니면
                if i == '.':  # '.'일 경우 stack 자체를 프린트
                    if len(stack) == 1:
                        print(*stack)
                    else: # stack이 비어있으면 error
                        print('error')
                else:
                    stack.append(int(i))