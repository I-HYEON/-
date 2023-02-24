'''
비트연산자 개념 배우고 오기
'''

arr = [3,6,7,1,5,4]

n = len(arr)

for i in range(1<<n): #1<<n은 부분집합의 개수
    for j in range(n):
        if i & (1<<j): #이부분이 해석이 안됨...
            print(arr[j],end=", ")
    print()
print()

