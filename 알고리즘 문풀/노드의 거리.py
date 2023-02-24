'''
0. argument로 출발 노드를 받아와서, 종료 노드를 만날때까지 너비우선탐색을 하는 함수
1. 출발노드를 큐에 넣고 시작한다. 방문 기록을 1로 초기화
2. while 문으로 탐색을 시작한다.(실행조건 : 큐가 남아있을 때)
2-1. 큐의 인덱스0값을 팝한 것이 현재노드(now).
2-2. 현재노드의 인접리스트를 읽어와 탐색 안한 곳이 있으면 방문기록을 남기고, 큐에 넣는다.
     이 때 만약, 읽어온 인접 노드가 종료노드랑 일치하면 현재노드의 방문기록을 반환한다.
2-3. while 문이 실행될때마다 큐의 제일 앞에 있는 노드의
     인접 노드를 탐색해서 방문 안한 곳이 있으면 큐에 추가되는 방식이며,
     계속 돌다가 인접노드가 이미 방문한 곳밖에 없으면 더이상 큐에 추가되지 않으므로
     이 때 while 문이 끝난다.
3.while 문이 끝나버리면 전부 탐색했는데, 종료노드에 도달하지 못했다는 거니까 0을 반환한다.
'''

def bfs(start_node):
    Q = [start_node] # 출발 노드를 큐에 넣음
    visited[start_node] = 1 # 출발 노드의 방문기록에 1을 남김
    while Q:  # 큐에 원소가 남아있으면 반복
        now = Q.pop(0)  # 큐의 맨 앞 원소를 받아옴
        for i in adj[now]:
            if visited[i] == 0:
                if i == end:
                    return visited[now]
                visited[i] = visited[now] + 1
                Q.append(i)
    return 0

T = int(input())

for tc in range(1,T+1):

    V,E = map(int,input().split())

    adj = [[] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]

    for _ in range(E):
        i,j = map(int,input().split())
        adj[i].append(j)
        adj[j].append(i)

    start,end = map(int,input().split())

    ans = bfs(start)
    print(f'#{tc}',ans)