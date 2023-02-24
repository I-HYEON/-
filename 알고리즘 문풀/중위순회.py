ans = []
def inorder(x):
    if x:
        lft = inorder(left_child[x])
        rgt = inorder(right_child[x])
        return str(lft) + tree[x]+str(rgt)
    else:
        return ''

for tc in range(1,11):
    N = int(input())
    words = [0 for _ in range(N+1)]
    left_child = [0 for _ in range(N+1)]
    right_child = [0 for _ in range(N+1)]
    for i in range(N):
        lst = list(input().split())
        if len(lst) >= 3:
            left_child[int(lst[0])] = int(lst[2])
        if len(lst) >= 4:
            right_child[int(lst[1])] = int(lst[3])

    words = inorder(1)
    ans.append(words)

for i in range(len(ans)):
    print(f'#{tc}',ans[i])