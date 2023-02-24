def postorder(x):  # 후위순회함수
    global fomula
    if 0 < x <= N:  # 해당 노드가 N보다 작거나 같으면
        postorder(left[x])  # 해당 노드의 왼쪽 자식을 먼저 호출하고
        postorder(right[x])  # 해당 노드의 오른쪽 자식을 호출해줘
        fomula.append(parents[x])  # fomula에 해당 노드에 담긴 값을 넣어줘
    return

for tc in range(1,11):  # 테스트 케이스 돌리기

    N = int(input())
    input_lst = []
    for _ in range(N):
        input_lst.append(list(input().split()))
    parents = [0] * (N+1)
    left = [0 for _ in range(N+1)]  # 왼쪽 자식 저장할 리스트
    right = [0 for _ in range(N+1)]  # 오른쪽 자식 저장할 리스트

    for l in input_lst:
        if len(l) >= 4:
            parents[int(l[0])] = l[1]  # 부모인덱스 기준으로 부모 원소 저장
            left[int(l[0])] = int(l[2])  # 부모인덱스 기준으로 왼쪽 자식 저장
            right[int(l[0])] = int(l[3])  # 부모인덱스 기준으로 오른쪽 자식 저장
        else:
            parents[int(l[0])] = int(l[1])  # 길이가 2일 때는 자식이 없으므로, 부모원소만 저장

    # 여기까지 parents에는 정점 번호 순서대로 부모노드 담겨있고, left,right에는 부모인덱스 기준으로 자식들이 담겨있음

    fomula = []
    postorder(1)

    # 여기까지하면 후위표기식이 완성됨
    # 아래는 후위표기식 계산

    stack = []
    for f in fomula:
        if str(type(f)) == "<class 'int'>":  # 피연산자를 만나면 스택에 담아줘
            stack.append(f)
        elif stack and f == '+':  # (스택에 피연산자가 남아있고) 연산자를 만나면 연산해줘
            stack.append(stack.pop(-2)+stack.pop(-1))
        elif stack and f == '-':
            stack.append(stack.pop(-2) - stack.pop(-1))
        elif stack and f == '*':
            stack.append(stack.pop(-2) * stack.pop(-1))
        elif stack and f == '/':
            stack.append(stack.pop(-2) / stack.pop(-1))

    print(f'#{tc}',int(stack[0]))  # 스택에 남은 정답을 정수형으로 변환해서 출력