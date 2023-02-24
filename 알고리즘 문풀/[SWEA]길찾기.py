for _ in range(10):
    tc, N = map(int, input().split())
    lst = list(map(int,input().split()))

    test = [[]for i in range(100)]
    for i in range(len(lst)):
        if i%2:
            test[lst[i-1]].append(lst[i])
        else:
            pass

    # print(test)

    ans = ''
    def dfs(graph, node, visited):
        global ans
        visited[node] = True
        ans += (str(node)+',')
        for i in graph[node]:
            if not visited[i]:
                dfs(graph, i, visited)

        return ans


    visit = [False] * 100


    if '99' in dfs(test, 0, visit):
        result = 1
    else:
        result = 0

    print(f'#{tc} {result}')