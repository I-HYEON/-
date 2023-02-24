#해당 위치에 둘 수 있으면 True, 둘 수 없으면 False를 반환하는 함수를 만듦
#좌표를 돌면서 둘 수 있으면 ans에 1을 더하고 둘 수 없으면 다음 인덱스로 가는 포문을 만든다.
N = int(input())
row = [0 for i in range(N)]

def ispromising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i] == abs(x-i)):
            return False

    return True

for i in range(N):
    row[1] = i
    if ispromising(1):
        ans += 1
