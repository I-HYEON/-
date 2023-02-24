def bfs(start,end):  # 출발노드, 도착노드 필요

    q = [s]  # 시작노드를 일단 큐에 담는다

    while q: # 큐가 남아있으면 계속 탐색
        next_node = q.pop(0)
        if next_node == end:
            return

        for i in graph[next_node]:
            if not visited[i]:  # 인접노드가 아직 방문 안한 곳이면
                q.append(i)  # 방문해봐야하므로 q에 넣어준다
                # 방문표시할 때, 현재노드까지의 거리에 1을 더해준 값을 넣는다
                visited[i] = visited[next_node] + 1

T = int(input())  # 테스트 케이스 개수
for tc in range(1,T+1):
    V,E = map(int,input().split())  # 노드 개수, 간선 개수
    graph = [[] for _ in range(V+1)]  # 인접리스트 생성
    for _ in range(E):  # 간선 수만큼 반복해서 그래프에 인접 노드 기록
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    s,e = map(int,input().split())
    visited = [0] * (V+1)  # 출발점부터의 거리 저장할 리스트(??)

    bfs(s,e)

    print(f'#{tc}',visited[e])