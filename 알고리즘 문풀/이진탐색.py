def inorder(node):
    global num

    if node <= N:
        inorder(node*2)
        tree[node] = num
        num += 1
        inorder(node*2 + 1)
    return

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    tree = [0 for i in range(N+1)]
    num = 1
    inorder(1)

    print(f'#{tc} {tree[1]} {tree[N//2]}')