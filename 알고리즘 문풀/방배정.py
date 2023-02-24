'''
학생들이 있고, 학생 정보가 (성별, 학년)으로 주어진다. 방의 최대인원도 주어진다.
같은 성별 끼리 그리고 같은 학년끼리만 방을 쓸수 있고, 정해진 최대인원을 넘길 수 없다.
조건에 맞게 모든 학생을 배정하기 위해 필요한 방의 최소개수를 구해야 함.

성별은 0~1로 2가지 경우,학년은 1~6으로 6가지 경우가 있어서 12가지 조합이 나온다.
이 모든 조합을 키로 갖는 딕셔너리를 생성해 학생들을 분류한다.
각각의 values(학생수)들을 최대인원 K로 나누어 필요한 방을 구하고, 다 더하면 필요한 총 방 개수를 알수 있다.
(나머지가 남으면 방은 무조건 하나 더 필요하므로 조건 필요)
'''
dict_key = []
for i in range(0,2):
    for j in range(1,7):
        dict_key.append((i,j))

mydict = {i:0 for i in dict_key}  # 학생 유형을 키 값으로하는 딕셔너리 생성

N, K = map(int,input().split())
for _ in range(N):
    A,B = map(int,input().split())
    mydict[(A,B)] += 1  # 학생 유형마다 몇명이 있는지 기록된 딕셔너리 완성

ans_list = list(map(lambda x:x//K+1 if x%K else x//K,mydict.values()))
print(sum(ans_list))