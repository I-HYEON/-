'''
트리정보가 주어진다.
N은 정점의 개수이므로
부모노드(연산자)를 기준으로 자식 노드 정보를 만든다.
'''
for tc in range(1,11):
    N = int(input())
    input_lst = []
    for _ in range(N):
        input_lst.append(list(input().split()))
    parents = [0] * (N+1)
    child = [[] for _ in range(N+1)]
    # parents에 부모노드 저장할 공간 마련, child에 부모노드 인덱스 기준으로 자식노드 저장할 공간 마련
    for l in input_lst:
        if len(l) >= 4:
            parents[int(l[0])] = l[1]
            child[int(l[0])].append(int(l[2]))
            child[int(l[0])].append(int(l[3]))
        else:
            parents[int(l[0])] = int(l[1])
    # parents에는 정점 번호 순서대로 부모노드 담겨있고, child에는 부모의 자식들이 담겨있음

    # print(parents)
    # print(child)

    def postorder(x):  # 후위순회함수

        if 0 < x <= N:  # 해당 노드가 N보다 작으면
            if child[x]:
                postorder(child[x][0])  # 해당 노드의 왼쪽 자식을 먼저 호출하고
                postorder(child[x][1])  # 해당 노드의 오른쪽 자식을 호출해줘
            print(parents[x])
        return

    postorder(1)
    print('end')