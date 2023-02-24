def preorder(parents_node):
    global cnt
    if parents_node:
        cnt += 1
        preorder(left_child[parents_node])
        preorder(right_child[parents_node])


T = int(input())
for tc in range(1,T+1):
    E,N = map(int,input().split())  # E는 간선의 수. 노드는 E+1 개수이므로 노드 개수를 알 수 있다.
    lst = list(map(int,input().split()))
    # 2, 1, 2, 5, 1, 6, 5, 3, 6, 4

    left_child = [0 for i in range(E+2)]
    right_child = [0 for i in range(E+2)]
    for i in range(0,len(lst)-1,2):
        p = lst[i]
        c = lst[i+1]
        if left_child[p]:
            right_child[p] = c
        else:
            left_child[p] = c
    cnt = 0

    preorder(N)
    print(f'#{tc}',cnt)