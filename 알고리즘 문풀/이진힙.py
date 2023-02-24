T = int(input())

def heap_sort(arr):
    for child in range(len(arr)-1,-1,-1):  # i는 0 ~ N-1(정렬하려는 리스트의 크기 N개)
        while (child-1)//2 >= 0:  # 부모노드 인덱스가 0보다 크면 계속 반복한다.
            if arr[(child-1)//2] > arr[child]:
                arr[(child-1)//2], arr[child] = arr[child],arr[(child-1)//2]
            child = (child-1)//2
    return arr

for tc in range(1,T+1):
    N = int(input())
    lst = []
    for i in map(int,input().split()):
        lst.append(i)
        lst = heap_sort(lst)

    sum = 0
    start = len(lst)-1
    while (start-1)//2 >= 0:
        sum += lst[(start-1)//2]
        start = (start-1)//2

    print(f'#{tc}',sum)