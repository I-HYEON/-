T = int(input())

def cal(x):
    if x * 2 <= N:
        cal(x * 2)
        cal(x * 2 + 1)
        if x * 2 + 1 > N:
            tree[x] = tree[x * 2]
        else:
            tree[x] = tree[x * 2] + tree[x * 2 + 1]
    return


for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = [0 for _ in range(N + 1)]
    for _ in range(M):
        leaf_node, l = map(int, input().split())
        tree[leaf_node] = l

    cal(1)
    print(f'#{tc}', tree[L])