T = int(input())

for tc in range(1,T+1):
    V,E = map(int, input().split())
    lst = [[]for i in range(V+1)]

    for i in range(E):
        A, B = map(int, input().split())
        lst[A].append(B)
    # print(lst)

    # s 출발노드를 제공했을때 모든 경로 탐색한 결과를 내게 하고 g가 그안에 있으면 1 없으면 0
    ans = ''

    def dfs(graph, node, visited):
        global ans
        visited[node] = True
        ans += str(node)
        for i in graph[node]:
            if not visited[i]:
                dfs(graph, i, visited)

        return ans

    S, G = map(int, input().split())

    visit = [False]*(V+1)

    if str(G) in str(dfs(lst,S,visit)):
        result = 1
    else:
        result = 0

    print(f'#{tc} {result}')