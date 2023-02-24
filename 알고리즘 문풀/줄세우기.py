'''
[0,1,2,3,4,5]
[0,0,1,1,3,2]
'''
N= int(input())
lst = [0] + list(map(int,input().split()))

ans_list = [1]
for i in range(len(lst)):
    if i <= 1:
        pass
    else:
        ans_list.insert(len(ans_list)-lst[i],i)

print(*ans_list)