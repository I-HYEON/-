'''
각 원소가 부분집합에 포함되었는지를 loop 이용하여 확인하고 부분집합을 생성하는 방법

{1,2,3,4} 부분집합을 만들려면
길이에 대응하는 리스트를 만들어서
0,0,0,0 이면 공집합
0,0,0,1 이면 원소가 4만있는 집합
0,0,1,1 이면 원소가 3,4가 있는 집합
이렇게 되는 셈이다

결론:각 원소의 포함여부를 확인하는 리스트를 만들고 해당 인덱스가 1이면
집합의 원소가 포함되어 있는 걸로 본다. 집합의 같은 인덱스를 가져오면 부분집합이 완성된다.
'''

A = [1,2,3,4]
bit = [0,0,0,0]

for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = j
                print(bit, end='')
                for p in range(4):
                    if bit[p]:
                        print(A[p], end=' ')
                print()

#이해가 안가는데,,,