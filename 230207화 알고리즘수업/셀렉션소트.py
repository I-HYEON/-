N = int(input())

arr = list(map(int,input().split()))


for i in range(N-1):
    minIdx = i
    for j in range(i+1,N):
        if arr[minIdx] > arr[j]:
            minIdx = j
    arr[minIdx], arr[i] = arr[i], arr[minIdx]

print(arr)