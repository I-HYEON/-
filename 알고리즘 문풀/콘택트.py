def contact(start):
    Q = []
    visited = [0] * 101
    ans = start

    Q.append(start)
    visited[start] = 1

    while Q:
        next = Q.pop(0)
        if visited[ans] < visited[next] or visited[ans] == visited[next] and ans<next:
            ans = next

        for n in adj_list[next]:
            if visited[n] == 0:
                Q.append(n)
                visited[n] = visited[next] + 1
    return ans

for tc in range(1,11):
    N,S = map(int,input().split())
    lst = list(map(int,input().split()))

    adj_list = [[] for _ in range(max(lst)+2)]
    for i in range(N//2):
        node = lst[i*2]
        adj_node = lst[i*2+1]
        adj_list[node].append(adj_node)

    print(f'#{tc}',contact(S))