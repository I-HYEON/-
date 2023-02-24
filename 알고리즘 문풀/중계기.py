'''
NN 정사각형 모양의 어느 한 마을에 각각의 집에 중계기를 설치
마을에 있는 모든 집들이 중계기 범위안에 포함되도록 하면서도 범위를 최소화하고 싶음
마을에 있는 집위치와 중계기 위치가 각각 1과 2로 주어짐.
마을의 모든 집들을 포함시킬 수 있는 중계기 통신범위의 반지름의 최소값을 구하라

우선, T(테스트케이스),N(마을의크기),hometown(마을배열)을 받아온다.
home_list에 1이 있는 즉, 집의 좌표를 담는다
repeater에 2가 있는 즉, 중계기 좌표를 담는다

반지름 r의 크기를 순회한다(range(1,??)로 설정)
 - 홈리스트의 좌표를 순회하면서, 중계기 범위에 들어와있는지 확인한다. 하나라도 벗어나면 해당 R은 포기한다.
 - 홈리스트의 좌표를 무사히 순회했을때, 해당 R이 답이 된다.
'''

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    hometown = [list(map(int,input().split())) for _ in range(N+1)]

    list_home = []
    for i in range(N+1):
        for j in range(N+1):
            if hometown[i][j] == 1:
                list_home.append((i,j))  # 집 좌표들을 리스트홈에 담아둠
            elif hometown[i][j] == 2:
                repeater = (i,j)  # 중계기 좌표를 리피터에 담아둠

    flag = True
    for r in range(1,16):
        for hi,hj in list_home:  # 집들이 범위안에 들어와 있는지 순회하면서 확인
            if (hi-repeater[0])**2 + (hj-repeater[1])**2 > r**2:  # 벗어나있으면
                break         # 다른 집들을 순회하는 것을 그만하고 다음 r로 넘어간다.
        else:  # 모든 집들이 벗어나지 않고 범위 내에 있으면
            ans = r  # 그 때의 반지름이 최소 반지름이므로 ans 에 넣고
            break  # 다음 r을 확인하는걸 중지

    print(f'#{tc}', ans)