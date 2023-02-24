'''
딱지놀이의 라운드 결과값을 출력해야 함

R에 총 라운드 수를 입력받는다
두줄씩 R번 반복하며 A와 B의 카드를 입력받는다.
'''

R = int(input())
for r in range(R):
    A,*A_list = map(int,input().split())
    B,*B_list = map(int,input().split())
    if A_list.count(4) > B_list.count(4):
        print('A')
    elif A_list.count(4) < B_list.count(4):
        print('B')
    else:
        if A_list.count(3) > B_list.count(3):
            print('A')
        elif A_list.count(3) < B_list.count(3):
            print('B')
        else:
            if A_list.count(2) > B_list.count(2):
                print('A')
            elif A_list.count(2) < B_list.count(2):
                print('B')
            else:
                if A_list.count(1) > B_list.count(1):
                    print('A')
                elif A_list.count(1) < B_list.count(1):
                    print('B')
                else:
                    print('D')